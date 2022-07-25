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

## Create Source
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

`gsutil iam ch serviceAccount:${SERVICE_ACCOUNT}:objectViewer gs://${PROJECT_ID}`

`gcloud sql import sql ${MYSQL_INSTANCE} gs://${PROJECT_ID}/resources/create_mysql.sql --quiet`


## Create Bucket
Create a bucket and have it post creation notifications to the topic, once it's created.
`gsutil mb gs://${PROJECT_ID}`

`gsutil cp create_mysql.sql gs://${PROJECT_ID}/resources/create_mysql.sql`

__Review dependency before running__ `gsutil notification create -f "json" -p "data/" -t "${TOPIC}" "gs://${PROJECT_ID}"`


## Create Pub/Sub Topic and Subscription
`gcloud pubsub topics create $TOPIC`

`gcloud pubsub subscriptions create $SUBSCRIPTION --topic=$TOPIC`

## Create Datastream Profile Definitions
`gcloud services enable datastream.googleapis.com`

Create the DB and Storage profiles.

#TODO Remove after fixed -- Remember User/PW must match source

```
gcloud datastream connection-profiles create ${SOURCE_MYSQL_PROFILE} \
          --location=us-central1 --type=mysql \
          --mysql-password=password123 --mysql-username=root \
          --display-name=${SOURCE_MYSQL_PROFILE} --mysql-hostname=${DB_IP_ADDRESS} \
          --mysql-port=3306 --static-ip-connectivity
```

```
gcloud datastream connection-profiles create ${DEST_GCS_PROFILE} \
          --location=us-central1 --type=google-cloud-storage \
          --bucket=$BUCKET --root-path=/root/path \
          --display-name=${DEST_GCS_PROFILE}
```


## Create Datastream Stream

__Review dependency before running__ Create the stream

## Craete BQ Dataset

`bq mk dataset`

## Deploy Dataflow Job

```
gcloud beta dataflow flex-template run datastream-replication \
        --project="${PROJECT_ID}" --region="us-central1" \
        --template-file-gcs-location="gs://dataflow-templates-us-central1/latest/flex/Cloud_Datastream_to_BigQuery" \
        --enable-streaming-engine \
        --parameters \
inputFilePattern="gs://${PROJECT_ID}/data/",\
gcsPubSubSubscription="projects/${PROJECT_ID}/subscriptions/${SUBSCRIPTION}
outputStagingTableNameTemplate="{_metadata_schema}_{_metadata_table}_log",\
outputTableNameTemplate="{_metadata_schema}_{_metadata_table}",\
deadLetterQueueDirectory="gs://${PROJECT_ID}/dlq/",\
maxNumWorkers=2,\
autoscalingAlgorithm="THROUGHPUT_BASED",\
mergeFrequencyMinutes=2,\
inputFileFormat="avro"
```


# Review Results

Review the data in BQ preview and you're done.