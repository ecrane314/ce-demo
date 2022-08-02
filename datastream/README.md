Based on https://www.cloudskillsboost.google/focuses/22949?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=16156042 

# Background

There are six componenets in this demo of data replication from a CloudSQL source into BigQuery for analytis.
`Source DB - Datastream - Dataflow - BQ - GCS - Pub/Sub`
Source hosts live OLTP stream and in CDC capable
Datastream creates a CDC collector and deploys it to Dataflow
The stream uses GCS and Pub/Sub for staging temp and in-flight data.

# Steps

1. Create Source
1. Create Bucket
1. Create Pub/Sub Topic and Subscription
1. Create Datastream Definitions
1. Create Datastream Stream
1. Craete BQ Dataset
1. Deploy Dataflow Job

# Part I
## Create Source
In cloudshell, git clone this repo
On two different tabs, source config.sh

```
gcloud sql instances create ${MYSQL_INSTANCE} \
    --cpu=2 --memory=10GB \
    --authorized-networks=${DATASTREAM_IPS} \
    --enable-bin-log \
    --region=us-central1 \
    --database-version=MYSQL_8_0 \
    --root-password password123
```

__Review dependency before running__ 

`source config2.sh` Remember `source config*` doesn't work correctly and 2 must be done after some prereqs are created

`gsutil iam ch serviceAccount:${SERVICE_ACCOUNT}:objectViewer $BUCKET`

`gcloud sql import sql ${MYSQL_INSTANCE} gs://${PROJECT_ID}/resources/create_mysql.sql --quiet`


## Create Bucket
Create a bucket and have it post creation notifications to the topic, once it's created.

`gsutil mb gs://${PROJECT_ID}`

`gsutil cp create_mysql.sql gs://${PROJECT_ID}/resources/create_mysql.sql`

__Review dependency before running__ 

`gsutil notification create -f "json" -p "data/" -t "${TOPIC}" "$BUCKET"`


## Create Pub/Sub Topic and Subscription
`gcloud pubsub topics create $TOPIC`

`gcloud pubsub subscriptions create $SUBSCRIPTION --topic=$TOPIC`

# Part II
## Create Datastream Profile Definitions
`gcloud services enable datastream.googleapis.com`

Create the DB and Storage profiles.

#TODO Remove after fixed -- Remember User/PW must match source


__Review dependency before running__ 

```
gcloud datastream connection-profiles create ${SRC_MYSQL_PROFILE} \
          --location=us-central1 --type=mysql \
          --mysql-password=password123 --mysql-username=root \
          --display-name=${SRC_MYSQL_PROFILE} --mysql-hostname $DB_IP_ADDRESS \
          --mysql-port=3306 --static-ip-connectivity
```

Datastream does not handle the gs:// prefix so we just use the bucket name. In this case, that's our project name.

```
gcloud datastream connection-profiles create ${DEST_GCS_PROFILE} \
          --location=us-central1 --type=google-cloud-storage \
          --bucket=$PROJECT_ID --root-path=/path \
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

`gcloud datastream streams update $STREAM --location=us-central1 \
          --state=RUNNING --update-mask=state`

## Craete BQ Dataset

`bq mk dataset-landing`

## Deploy Dataflow Job

`gcloud services enable dataflow.googleapis.com`

#TODO this doesn't work, doesn't submit correctly.

```
gcloud dataflow flex-template run datastream-replication \
--project="${PROJECT_ID}" --region="us-central1" \
--template-file-gcs-location="gs://dataflow-templates-us-central1/latest/flex/Cloud_Datastream_to_BigQuery" \
--enable-streaming-engine \
--parameters \
inputFilePattern="gs://${PROJECT_ID}/data/",\
gcsPubSubSubscription="projects/${PROJECT_ID}/subscriptions/${SUBSCRIPTION},\
outputProjectId="${PROJECT_ID}",\
outputStagingDatasetTemplate="dataset",\
outputDatasetTemplate="dataset",\
outputStagingTableNameTemplate="{_metadata_schema}_{_metadata_table}_log",\
outputTableNameTemplate="{_metadata_schema}_{_metadata_table}",\
deadLetterQueueDirectory="gs://${PROJECT_ID}/dlq/",\
maxNumWorkers=2,\
autoscalingAlgorithm="THROUGHPUT_BASED",\
mergeFrequencyMinutes=2,\
inputFileFormat='avro'

```


# Review Results

Review the data in BQ preview and you're done.
Nost Postgres coming soon.
Note the 'Future tables' option in the inclusion logic.
Notice the --backfill-all option.

#BUG The gcloud connection-profiles create might have a bug. Notice no '=' allowed on hostname
#BUG gcloud datastreams streams create doesn't work without --force flag

#BUG

```
student_00_360a81feeb6c@cloudshell:~ (qwiklabs-gcp-00-84ff77e57b16)$ gcloud datastream streams list --location us-central1
NAME: test-stream
STATE: NOT_STARTED
SOURCE: projects/469032676304/locations/us-central1/connectionProfiles/mysql-cp
DESTINATION: projects/469032676304/locations/us-central1/connectionProfiles/gcs-cp
CREATE_TIME: 2022-07-25T22:15:19.738781015Z
UPDATE_TIME: 2022-07-25T22:19:27.884373269Z


student_00_360a81feeb6c@cloudshell:~ (qwiklabs-gcp-00-84ff77e57b16)$ gcloud datastream routes list --location us-central1
ERROR: (gcloud.datastream.routes.list) argument --location: --private-connection must be specified.
Usage: gcloud datastream routes list (--private-connection=PRIVATE_CONNECTION : --location=LOCATION) [optional flags]
  optional flags may be  --filter | --help | --limit | --location |
                         --page-size | --sort-by | --uri

For detailed information on this command and its flags, run:
  gcloud datastream routes list --help
```


```
student_00_360a81feeb6c@cloudshell:~ (qwiklabs-gcp-00-84ff77e57b16)$ gcloud datastream streams list --location=us-central1
NAME: test-stream
STATE: NOT_STARTED
SOURCE: projects/469032676304/locations/us-central1/connectionProfiles/mysql-cp
DESTINATION: projects/469032676304/locations/us-central1/connectionProfiles/gcs-cp
CREATE_TIME: 2022-07-25T22:15:19.738781015Z
UPDATE_TIME: 2022-07-25T22:19:27.884373269Z

student_00_360a81feeb6c@cloudshell:~ (qwiklabs-gcp-00-84ff77e57b16)$ gcloud datastream routes list --location=us-central1
ERROR: (gcloud.datastream.routes.list) argument --location: --private-connection must be specified.
Usage: gcloud datastream routes list (--private-connection=PRIVATE_CONNECTION : --location=LOCATION) [optional flags]
  optional flags may be  --filter | --help | --limit | --location |
                         --page-size | --sort-by | --uri

For detailed information on this command and its flags, run:
  gcloud datastream routes list --help
```
