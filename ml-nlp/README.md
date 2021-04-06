#ml-nlp Demo with AutoML
https://cloud.google.com/natural-language/automl/docs/quickstart

Enable AutoML APIs
Create entity extraction dataset (or other adventure)
Using CSV from gs://cloud-ml-data/NL-entity/dataset.csv , the gs will be missing because they append. NOTE:
In unified, they ask for files with jsonl extension and you pick the split or automatic.
You'll need to gsutil copy that csv file or cat it and pull the fields and URIs

UPDATE: This didn't work in Unified, perfhaps formatting off

```
Operation ID:
projects/990799180178/locations/us-central1/operations/5280214376882634752
Error Messages:
Error: Could not parse the line, not a valid json: Cannot find field: annotations in message google.cloud.aiplatform.master.schema.TextExtractionIoFormat. for: gs://cloud-ml-data/NL-entity/train.jsonl line 295
Error: Could not parse the line, not a valid json: Cannot find field: annotations in message google.cloud.aiplatform.master.schema.TextExtractionIoFormat. for: gs://cloud-ml-data/NL-entity/train.jsonl line 395
Error: Could not parse the line, not a valid json: Cannot find field: annotations in message google.cloud.aiplatform.master.schema.TextExtractionIoFormat. for: gs://cloud-ml-data/NL-entity/train.jsonl line 95 
```

Switching to Classic AI Platform, AutoML Experience should be the same
Use the Natural Language options in GCP console tray, then create an entity dataset
https://console.cloud.google.com/natural-language?_ga=2.124070538.1266633889.1617667956-416308210.1591721327&authuser=2

Used file from https://pubmed.ncbi.nlm.nih.gov/32150360/ for testing. Downloaded pubmed format as txt
Available at gs://ce-demo1/pubmed_nlp_sample.txt

