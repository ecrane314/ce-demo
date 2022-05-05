# Cloud Functions
 
 - Set config
 - On deploy, set service account if needed for permissions
 - On deploy, gcfunction name must match entry function from source
 - On deploy, --trigger-bucket will be the bucket to 'watch' for new uploads
 - Build source will be zipped and copied as is to a GCS bucket
 - Function build artifacts will live in separate bucket
  gcloud functions deploy redact_gcs --region us-central1 --service-account \
        <svc@account.com> --trigger-bucket dlp-inbound --runtime python38
- https://cloud.google.com/functions/docs/calling/storage

- To deploy your function, run something like `gcloud functions deploy hello_get --region=us-central1 --runtime=python39 --trigger-http --ingress-settings=internal-and-gclb --allow-unauthenticated`

- `ingress_settings=all` may be restricted by your GCP Org admins. Try internal-and-gclb
 The allow unauthenticated is optional.

## [Functions Framework](https://pypi.org/project/functions-framework/)
Run main.py locally by pip installing functions-framework, and running
`functions_framework --target hello_get --debug`
