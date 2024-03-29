export PROJECT_ID=$(gcloud config get-value project)

export MYSQL_INSTANCE=mysql-db
export DATASTREAM_IPS=34.72.28.29,34.67.234.134,34.67.6.157,34.72.239.218,34.71.242.81
#TODO export PRV_SUBNET=

export TOPIC=datastream
export SUBSCRIPTION=datastream-subscription

export SRC_MYSQL_PROFILE=mysql-cp
export DEST_GCS_PROFILE=gcs-cp
export BUCKET=gs://${PROJECT_ID}
export STREAM=test-stream
export STREAM_SRC_CONFIG=mysql-source-config.json
export STREAM_DEST_CONFIG=gcs-destination-config.json

export DATASET=landing

export MYSQL_USER=root
export MYSQL_PASS=password123