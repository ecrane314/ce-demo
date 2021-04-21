"""
https://cloud.google.com/ai-platform-unified/docs/tutorials/text-classification-automl
My config in ~/.config/ce-demo

Prep
export BUCKET=${PROJECT_ID}-lcm
gsutil mb -p ${PROJECT_ID} -l us-central1 gs://${BUCKET}/
gsutil -m cp -R gs://cloud-ml-data/NL-classification/happiness.csv gs://${BUCKET}/text/
"""
