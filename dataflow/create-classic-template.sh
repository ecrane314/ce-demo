gcloud dataflow jobs run iotlabflow \
 --gcs-location gs://dataflow-templates-us-central1/latest/PubSub_to_BigQuery \
 --region us-central1 --staging-location gs://qwiklabs-gcp-02-7a5654fed8e0-bucket/tmp \
 --parameters inputTopic=projects/qwiklabs-gcp-02-7a5654fed8e0/topics/iotlab,outputTableSpec=qwiklabs-gcp-02-7a5654fed8e0:iotlabdataset.sensordata