"""
https://www.kaggle.com/dansbecker/getting-started-with-sql-and-bigquery
"""

from google.cloud import bigquery

# Create client
client = bigquery.Client()

# Create dataset reference
# cient.dataset() is deprecated, use dataset.DatasetReference()
# dataset_ref = client.dataset("austin_incidents", project="bigquery-public-data")
dataset_ref = bigquery.dataset.DatasetReference(dataset_id="austin_incidents", project="bigquery-public-data")

# Fetch details and enumerate
dataset = client.get_dataset(dataset_ref)
tables = client.list_tables(dataset)
for table in tables:
    print(table.table_id)

# Create table reference
table_ref = dataset_ref.table("incidents_2016")
