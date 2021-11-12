# Set PROJECT_ID   MY_REGION

gcloud iot registries create iotlab-registry \
    --project=$PROJECT_ID \
    --region=$MY_REGION \
    -event-notification-config=project/$PROJECT_ID/topics/iotlab
