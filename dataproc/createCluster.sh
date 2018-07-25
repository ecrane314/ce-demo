#[WIP] July 2018

export PROJECT_ID=$(gcloud config get-value project)
export BUCKET=$(gcloud config get-value project)
export REGION=us-central1
export ZONE=us-central1-c
export IP=$(curl -s v4.ifconfig.co)

#ipv6 possible in this case, not currently GCP compatible
#IP=$(curl -s ifconfig.co)

#These specs are from the coursera qwiklab
gcloud dataproc --region $REGION clusters create ce-demo-cluster \
--bucket $BUCKET --subnet default --zone $ZONE \
--master-machine-type n1-standard-2 --master-boot-disk-size 100 \
--num-workers 3 --worker-machine-type n1-standard-1 --worker-boot-disk-size 50 \
--image-version 1.2 --scopes 'https://www.googleapis.com/auth/cloud-platform' \
--tags hadoopaccess --project $PROJECT_ID

