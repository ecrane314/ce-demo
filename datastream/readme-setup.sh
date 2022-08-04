# Do the Instance setup first.

source config.sh

gsutil mb gs://${PROJECT_ID}

gsutil cp create_mysql.sql gs://${PROJECT_ID}/resources/create_mysql.sql


## Create Pub/Sub Topic and Subscription
gcloud pubsub topics create $TOPIC

gcloud pubsub subscriptions create $SUBSCRIPTION --topic=$TOPIC


## Create Object Notification to Topic
gsutil notification create -f "json" -p "data/" -t "${TOPIC}" "$BUCKET"

## Configure Bucket Permissions and Import SQL Data
source config2.sh

gsutil iam ch serviceAccount:${SERVICE_ACCOUNT}:objectViewer $BUCKET

gcloud sql import sql ${MYSQL_INSTANCE} gs://${PROJECT_ID}/resources/create_mysql.sql --quiet

# Part II
## Create Datastream Profile Definitions
gcloud services enable datastream.googleapis.com



gcloud datastream connection-profiles create ${SRC_MYSQL_PROFILE} \
          --location=us-central1 --type=mysql \
          --mysql-password=password123 --mysql-username=root \
          --display-name=${SRC_MYSQL_PROFILE} --mysql-hostname $DB_IP_ADDRESS \
          --mysql-port=3306 --static-ip-connectivity



gcloud datastream connection-profiles create ${DEST_GCS_PROFILE} \
          --location=us-central1 --type=google-cloud-storage \
          --bucket=$PROJECT_ID --root-path=/data \
          --display-name=${DEST_GCS_PROFILE}



## Create Datastream Stream


gcloud datastream streams create $STREAM --location=us-central1 \
          --display-name=$STREAM --source=$SRC_MYSQL_PROFILE \
          --mysql-source-config=$STREAM_SRC_CONFIG \
          --destination=$DEST_GCS_PROFILE \
          --gcs-destination-config=$STREAM_DEST_CONFIG \
          --backfill-all --force


gcloud datastream streams update $STREAM --location=us-central1\
          --state=RUNNING --update-mask=state

## Create BQ Dataset
#TODO make 'dataset' an env variable. Used several times in Dataflow parameters.
bq mk dataset

## Deploy Dataflow Job

gcloud services enable dataflow.googleapis.com