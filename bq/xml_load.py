#!/usr/bin/env python3
"""
Loading CSV Data Into BigQuery Table
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python
Preparation
1-- In IAM, set your service account access for GCS read/write and BQ write
2-- Use this export statement at shell to set your credentials before runtime
export GOOGLE_APPLICATION_CREDENTIALS=/home/MyHomeDir/<SERVICE ACCT PRV KEY>.json
3-- Export BigQuery public dataset table from marketplace to GCS in CSV
"""

from google.cloud import bigquery

# sample, override as desired
DATASETID = "bq_demo_set"
TABLEID = "xml_land"
SOURCEURI = ""


def load_bq_from_xml(dataset_id=DATASETID, gcs_uri=SOURCEURI,
                     table_id=TABLEID):
    """Submit a BigQuery load job which reads from GCS."""

    # Make your clients
    bq_client = bigquery.Client()



    # Pointer to our target dataset
    dataset_ref = bq_client.dataset(dataset_id)



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
    job_config.create_disposition = "CREATE_NEVER"



    load_job = bq_client.load_table_from_uri(
        gcs_uri, dataset_ref.table(table_id), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    # Waits for table load job to complete, inform us.
    load_job.result()
    print("Job finished.")



    # Show how many rows were landed
    destination_table = bq_client.get_table(dataset_ref.table(table_id))
    print("Loaded {} rows.".format(destination_table.num_rows))


if __name__ == "__main__":
    load_bq_from_xml(DATASETID)
