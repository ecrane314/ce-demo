#!/usr/bin/env python
"""
https://cloud.google.com/bigquery/docs/bigquery-storage-python-pandas
Use this export statement at shell to set your credentials before runtime
export GOOGLE_APPLICATION_CREDENTIALS=/home/evancrane/ce-demo2-bq-analyst.json
"""

import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1


# Get token using local credentials
credentials, your_project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)


# Make your clients
bqclient = bigquery.Client(
    credentials=credentials,
    project=your_project_id,
)
bqstorageclient = bigquery_storage_v1beta1.BigQueryStorageClient(
    credentials=credentials
)


def bq_query_results():
    """Submit a BigQuery job, store results in a pandas dataframe."""

    # Create a query
    query_string = """
    SELECT
    *
    FROM
    `nyc-tlc.yellow.trips`
    WHERE
    dropoff_longitude BETWEEN -74.02
    AND -74.001
    AND dropoff_latitude BETWEEN 40.73
    AND 40.75
    LIMIT
    1000   """



    dataframe = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(bqstorage_client=bqstorageclient)
    )

    print(dataframe.head(10))

if __name__ == "__main__":
    bq_query_results()
