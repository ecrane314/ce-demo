#  export SENSOR1  SENSOR2  PROJECT_ID  MY_REGION
# create key

gcloud iot devices create $SENSOR1 \
  --project=$PROJECT_ID \
  --region=$MY_REGION \
  --registry=iotlab-registry \
  --public-key path=rsa_cert.pem,type=rs256

gcloud iot devices create $SENSOR2 \
  --project=$PROJECT_ID \
  --region=$MY_REGION \
  --registry=iotlab-registry \
  --public-key path=rsa_cert.pem,type=rs256
