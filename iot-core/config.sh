#Config, at terminal, run   $ source config.sh
export MY_REGION=us-central1
export PROJECT_ID=$(gcloud config --quiet get-value project)
export REGISTRY=iot-demo-reg
export TOPIC=data-topic
export SUBSCRIPTION=data-sub
export DEVICE=geo-tracking
#export SENSOR1=temp-sensor-buenos-aires
#export SENSOR2=temp-sensor-buenos-istanbul
