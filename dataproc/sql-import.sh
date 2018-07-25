#!/bin/bash

#create and populate sql tables from schema snapshots and
#table data stored in a gcs bucket

#command line arg for instance name and bucket name
BUCKET=$2
INSTANCE=$1

#import bucket hosted table schema to sql instance
gcloud sql import sql $INSTANCE gs://${BUCKET}/sql/table_creation.sql

#populate table with sample data
gcloud sql import csv $INSTANCE gs://${BUCKET}/sql/recommendation_spark

${bucelet}accommodation.csv
database recommendation_spark
table Accommodation
