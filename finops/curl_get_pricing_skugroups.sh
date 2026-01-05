#!/usr/bin/env bash

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
"https://cloudbilling.googleapis.com/v1beta/skuGroups?pageSize=1000"

# "https://cloudbilling.googleapis.com/v1beta/billingAccounts/YOUR_BILLING_ACCOUNT_ID/skuGroups"
