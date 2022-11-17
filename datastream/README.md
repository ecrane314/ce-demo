Based on the Qwiklab here, with additional scripting and substitution of environment variables for simplicity. https://www.cloudskillsboost.google/focuses/22949?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=16156042 

# Background

There are six componenets in this demo of data replication from a CloudSQL source into BigQuery for analytis.
`Source MySQL DB - Datastream - GCS - Pub/Sub - Dataflow - BQ`
The source is a live OLTP db setup for binary logging and replication for CDC.
Datastream creates a CDC collector and posts the avro deltas to the bucket.
Notifications on the bucket post to a Pub/Sub topic.
Dataflow pulls on a subscription on that topic to get the gcs uris.
The Dataflow pipeline reads the files, confirms the headings, and writes to BQ or to the DLQ.

# Steps

1. Create Source
1. Create Bucket
1. Create Pub/Sub Topic and Subscription
1. Create Datastream Definitions
1. Create Datastream Stream
1. Craete BQ Dataset
1. Deploy Dataflow Job

# Part I
## Create Source [Option A]
In cloudshell, git clone this repo to get these config files and scripts.

`git clone https://github.com/ecrane314/ce-demo.git`

`cd ce-demo/datastream && source config.sh`

```
gcloud sql instances create ${MYSQL_INSTANCE} \
    --cpu=2 --memory=10GB \
    --authorized-networks=${DATASTREAM_IPS} \
    --enable-bin-log \
    --region=us-central1 \
    --database-version=MYSQL_8_0 \
    --root-password $MYSQL_PASS
```

## Create Source [Option B, Internal]
[Private Connectivity to Datastream](https://cloud.google.com/datastream/docs/private-connectivity).

#TODO Fix
```
gcloud sql instances create ${MYSQL_INSTANCE} \
    --cpu=2 --memory=10GB \
    --authorized-networks=${PRV_SUBNET} \
    --enable-bin-log \
    --region=us-central1 \
    --database-version=MYSQL_8_0 \
    --root-password $MYSQL_PASS
```

If you're using private networks, you'll need an intermediary machine running CloudSQL Auth Proxy to allow the Datastream workers to connect to your CloudSQL instance. SSH into your machine with access to the SQL instance and run the [Proxy Setup](https://cloud.google.com/sql/docs/mysql/sql-proxy) with those instructions to run in the background. 

Run `gcloud sql instances describe <name>` to get the connection string. Use the address on which you want to listen. For example, 10.0.0.2 because that's our address from DHCP and where we're listening for local connection requests. Then run the proxy with `nohup` and `&`. It will be listening for connections. Adding `nohup` to the front will redirect output to log and not clutter your workspace. To troubleshoot, don't use this and read output right on the screen. It may also let you run this and close out the terminal while keeping it running, though it may have already been updated to do this. Otherwise, consider running it as a service so it stays up.

`./cloud_sql_proxy -instances=ce-demo1:us-central1:mysql-db=tcp:10.0.0.2:3306 &`

While that's running... continue

[Install mysql client](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html) You'll need to setup `apt` source repo for mysql. You'll need to download the script from Oracle,
get it to your machine and run it to add the repo with the right keys.  Once done, install `sudo apt install mysql-client` to get the mysql client.

OR DOWNLOAD HERE http://dev.mysql.com/downloads/mysql/ . 

Once that's done, run 
`mysql -u $MYSQL_USER -p --host <proxy internal IP> --port 3306` to connect. See that the already running proxy recognized the new connection to your SQL source in the output.


## Spin Up Resources Below

Once the instance is live. Continue with the steps below OR run them all at once with the script `bash readme-setup.sh`. 

You're done, wait a few minutes then check BigQuery.


## Create Bucket
Create a bucket and have it post creation notifications to the topic, once it's created.

`gsutil mb gs://${PROJECT_ID}`

`gsutil cp create_mysql.sql gs://${PROJECT_ID}/resources/create_mysql.sql`


## Create Pub/Sub Topic and Subscription
`gcloud pubsub topics create $TOPIC`

`gcloud pubsub subscriptions create $SUBSCRIPTION --topic=$TOPIC`


## Create Object Notification to Topic
`gsutil notification create -f "json" -p "data/" -t "${TOPIC}" "$BUCKET"`

## Configure Bucket Permissions and Import SQL Data
`source config2.sh` Remember `source config*` doesn't work correctly and 2 must be done after some prereqs are created

`gsutil iam ch serviceAccount:${SERVICE_ACCOUNT}:objectViewer $BUCKET`

`gcloud sql import sql ${MYSQL_INSTANCE} gs://${PROJECT_ID}/resources/create_mysql.sql --quiet`

# Part II
## Create Datastream Profile Definitions
`gcloud services enable datastream.googleapis.com`

Create the DB and Storage profiles.


__Review dependency before running__ 

```
gcloud datastream connection-profiles create ${SRC_MYSQL_PROFILE} \
          --location=us-central1 --type=mysql \
          --mysql-password=$MYSQL_PASS --mysql-username=$MYSQL_USER \
          --display-name=${SRC_MYSQL_PROFILE} --mysql-hostname $DB_IP_ADDRESS \
          --mysql-port=3306 --static-ip-connectivity
```

If instead, your source is using private connectivity with VPC peering, you'll need to first establish an IP range in your VPC and establish a peer.

#TODO add the code for the above.

```
gcloud datastream connection-profiles create ${SRC_MYSQL_PROFILE} \
          --location=us-central1 --type=mysql \
          --mysql-password=$MYSQL_PASS --mysql-username=$MYSQL_USER \
          --display-name=${SRC_MYSQL_PROFILE} --mysql-hostname $DB_IP_ADDRESS \
          --mysql-port=3306 --<PEERING VERSION>
```

Datastream does not handle the gs:// prefix so we just use the bucket name. In this case, that's our project name.

```
gcloud datastream connection-profiles create ${DEST_GCS_PROFILE} \
          --location=us-central1 --type=google-cloud-storage \
          --bucket=$PROJECT_ID --root-path=/data \
          --display-name=${DEST_GCS_PROFILE}
```

Optionally, test your DB stream. The GCS will not have a test.

## Create Datastream Stream

Create the stream. Remember the json files must be updated to match your source.

```
gcloud datastream streams create $STREAM --location=us-central1 \
          --display-name=$STREAM --source=$SRC_MYSQL_PROFILE \
          --mysql-source-config=$STREAM_SRC_CONFIG \
          --destination=$DEST_GCS_PROFILE \
          --gcs-destination-config=$STREAM_DEST_CONFIG \
          --backfill-all --force
```

`gcloud datastream streams update $STREAM --location=us-central1\
          --state=RUNNING --update-mask=state`

## Create BQ Dataset

`bq mk $DATASET`

## Deploy Dataflow Job

`gcloud services enable dataflow.googleapis.com`

#TODO Blocked start because not shieldedVM

```
gcloud dataflow flex-template run datastream-replication2 \
--project="${PROJECT_ID}" --region="us-central1" \
--template-file-gcs-location="gs://dataflow-templates-us-central1/latest/flex/Cloud_Datastream_to_BigQuery" \
--enable-streaming-engine \
--parameters=\
inputFilePattern="gs://${PROJECT_ID}/data/",\
gcsPubSubSubscription="projects/${PROJECT_ID}/subscriptions/${SUBSCRIPTION}",\
outputProjectId="${PROJECT_ID}",\
outputStagingDatasetTemplate="$DATASET",\
outputDatasetTemplate="$DATASET",\
outputStagingTableNameTemplate="{_metadata_schema}_{_metadata_table}_log",\
outputTableNameTemplate="{_metadata_schema}_{_metadata_table}",\
deadLetterQueueDirectory="gs://${PROJECT_ID}/dlq/",\
maxNumWorkers=2,\
autoscalingAlgorithm="THROUGHPUT_BASED",\
mergeFrequencyMinutes=2,\
inputFileFormat="avro"
```


# Review Results

1. Review the data in BQ preview and you're done. You may need to hard refresh the BQ UI to see the tables.
1. Try using the create_mysql.sql to create a new record and see results.
1. Note the 'Future tables' option in the inclusion logic. There is behavior defined on how existing table schema changes will be handled.
Notice the --backfill-all option. Backfill and sync are charged at different rates.
1. Note Postgres coming soon. (as of Aug 2022)


Fixed--- The `gcloud connection-profiles create` might have a bug. Notice no '=' allowed on hostname, throws error.
#BUG gcloud datastreams streams create doesn't work without --force flag
#BUG the gs:// prefix is not handled but does NOT throw an error even though it's invalid. You can click it in the Datastream UI and the GCS ui will tell you it's invalid.
