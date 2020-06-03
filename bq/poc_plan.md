<!-- https://guides.github.com/features/mastering-markdown/ -->

# BigQuery Ingestion


### Option 1 User GUI Upload
1. `console.cloud.google.com`
2. In storage view, upload your `.csv` or `.avro` etc. to a bucket
3. In BigQuery, create a dataset
4. Create a table and specify your uploaded file as the source

### Option 2 Client Library (python3)
Use the `load_job.py` script as a guide to ingest gcs flat files to bq

### Option 3 GUI ETL

#### 3a Use Dataprep and Dataflow
Use [Cloud Dataprep](https://cloud.google.com/dataprep/docs/html/Using-BigQuery_59736092) to createa a DataFlow job to ingest data from GCS to BQ

#### 3b Use Data Fusion (CDAP)
Land your data into BigQuery using the [Cloud Data Fusion](https://cloud.google.com/data-fusion) UI.

### Option 4 Third party tools
Tools like Informatica, Matillion, and others from the [Google Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:service&filter=category:big-data)