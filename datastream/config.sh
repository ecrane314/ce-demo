export PROJECT_ID=$(gcloud config get-value project)
export MYSQL_INSTANCE=mysql-db
export DATASTREAM_IPS=34.72.28.29,34.67.234.134,34.67.6.157,34.72.239.218,34.71.242.81
export TOPIC=datastream
export SUBSCRIPTION=datastream-subscription
export SOURCE_MYSQL_PROFILE=mysql-cp
export DEST_GCS_PROFILE=gcs-cp
export BUCKET=gs://${PROJECT_ID}

#TODO MYSQL_USER=  In creation of DB and DS Profile
#TODO MYSQL_PASS=