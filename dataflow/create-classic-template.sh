
gcloud dataflow jobs run iotlabflow \
--gcs-location gs://dataflow-templates-us-central1/latest/PubSub_to_BigQuery \
--region us-central1 --staging-location gs://qwiklabs-gcp-03-e5549ab3ea29-bucket/tmp \
--parameters inputTopic=projects/qwiklabs-gcp-03-e5549ab3ea29/topics/iotlab,outputTableSpec=qwiklabs-gcp-03-e5549ab3ea29:iotlabdataset.sensordata

