#!/usr/bin/env python
"""
Loading CSV Data Into BigQuery Table
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python
Preparation
1-- In IAM, set your service account access for GCS read/write and BQ write
2-- Use this export statement at shell to set your credentials before runtime
export GOOGLE_APPLICATION_CREDENTIALS=/home/MyHomeDir/<SERVICE ACCT PRV KEY>.json
3-- Export BigQuery public dataset table from marketplace to GCS in CSV
"""

import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1
#from google.cloud import storage

#Can override this default at runtime
DATASETID = "bq_demo_set"
TABLEID = "icoad_2005_dst"
SOURCEURI = "gs://ce-demo2/bq/icoads_core_2005-*.csv"

print(DATASETID + " ==break point DATASETID pre func")
print(TABLEID + " ==break point TABLEID pre func")
print(SOURCEURI + " ==break point SOURCEURI pre func")


def load_bq_from_gcs(dataset_id = DATASETID, gcs_uri = "gs://ce-demo2/bq/icoads_core_2005-*.csv",
    table_id = TABLEID):
    """Submit a BigQuery load job which reads from GCS."""

    print("===============")
    print(SOURCEURI + " ==break point SOURCEURI begin func")
    print(gcs_uri + " ==break point gcs_uri begin func")

    print(DATASETID + " ==break point DATASETID begin func")
    print(dataset_id + " ==break point dataset_id begin func")

    print(TABLEID + " ==break point TABLEID begin func")
    print(table_id + " ==break point table_id begin func")
    print("===============")


    # Get token using local credentials
    credentials, your_project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    # Make your clients
    bq_client = bigquery.Client(
        credentials=credentials,
        project=your_project_id,
    )
    #storage_client = storage.Client()
    #bq_storage_client = bigquery_storage_v1beta1.BigQueryStorageClient(
    #    credentials=credentials
    #)

    # Pointer to our target dataset
    dataset_ref = bq_client.dataset(dataset_id)
    
    print(gcs_uri + " ==break point clients made, job not yet configured")

    # Create our load job configuration and define schema inline
    job_config = bigquery.LoadJobConfig()
    #TODO form and load external json schema file
    #job_config.schema = [
    #   bigquery.SchemaField("name", "STRING"),
    #   bigquery.SchemaField("post_abbr", "STRING"),
    #]
    job_config.autodetect = True
    
    # Leading row of csv input are headers
    job_config.skip_leading_rows = 1
    
    # The source format defaults to CSV, so the line below is optional.
    job_config.source_format = bigquery.SourceFormat.CSV

    print(gcs_uri + " ==break point")
    load_job = bq_client.load_table_from_uri(
        gcs_uri, dataset_ref.table(table_id), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))


    load_job.result()  # Waits for table load to complete.
    print("Job finished.")


    destination_table = bq_client.get_table(dataset_ref.table(table_id))
    print("Loaded {} rows.".format(destination_table.num_rows))



if __name__ == "__main__":
    load_bq_from_gcs(DATASETID)
