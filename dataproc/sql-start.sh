#!/bin/bash

# cloud shell calling source IP is fetched from website to authorize for SQL
# unclear if root password can be set from initialization

gcloud sql instances create rentals --assign-ip \
--authorized-networks=$(curl -s https://canihazip.com/s)/32 \
--database-version=MYSQL_5_7 --region=us-central1 --storage-size=10
