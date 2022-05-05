# Cloud Functions

To deploy your function, run something like `gcloud functions deploy HELLO_FUNC --region=us-central1 --runtime=python39 --trigger-http --ingress-settings=all --allow-unauthenticated`

 INGRESS SETTINGS may be restricted by your GCP Org admins. The allow unauthenticated is optional.