### Katas Notes and Hints to Myself

1. Case sensitive, beam.create != beam.Create
1. DoFn classes, you must override process function eg def process(self, element)
1. Map gets passed the name of a function, but ParDo you need to call the constructor ie class() which extends DoFn.
1. beam.Map 1:1 and beam.Flatmap 1:M often use lambda and are simplifications of DoFn
1. functions and classes can be defined within functions
1. PColls are descriptions of operations, can't be directly written to files or manipulated. 
1. Only make sense in context of a ptransform
1. Remember tuples are immutable and lists not. Place tuples inside of lists for added capability
1. Using index [0] in a function which is used in a beam.Map() call means each element gets called. Eg CoGroupByKey result is passed to a map function, each item will become [0] for a call to the function.
1. beam.CombineFn() defines how to work on data, then CombineGlobally is used in the pipeline to call your CombineFn. CombineGlobally(CombineFn())
1. A. For each batch, the create_accumulator method is invoked to create a fresh initial "accumulator" value representing the combination of zero values.
 B. For each input value in the batch, the add_input method is invoked to combine more values with the accumulator for that batch.
C. The merge_accumulators method is invoked to combine accumulators from separate batches into a single combined output accumulator value, once all of the accumulators have had all the input value in their batches added to them. This operation is invoked repeatedly, until there is only one accumulator value left.
D. The extract_output operation is invoked on the final accumulator to get the output value.
1. Partition must know number of parts at graph construction time. Can't calculate midway
1. zip(list1, list2) packs it up and zip(*lists) unpacks it. Works also on lists NOT craeted with zip
1. zip is not idempotent and can be consumed. list(<zip object>) returns the list, then [] second time

# [Beam] Pipeline Options
1. Dump schema from current table
      In my example that's BigQuery... strip down to columsn I wants
      bq show --schema --format prettyjson bigquery-public-data:austin_311.311_request > schema.json
      drop columns, adjust descriptions, names, and types

1. If couldn't dump to file, create your json schema file with the schema specs
      https://cloud.google.com/bigquery/docs/schemas#specifying_a_json_schema_file


1. Run from gcloud 
```
gcloud dataflow jobs run 20201109-003 \
--gcs-location gs://dataflow-templates/latest/GCS_Text_to_BigQuery \
--region=us-central1 --network=custom-vpc --subnetwork=regions/us-central1/subnetworks/sn-central1 \
--parameters \
javascriptTextTransformFunctionName=transform,\
JSONPath=gs://ce-demo2/dataflow/311_request_schema.json,\
javascriptTextTransformGcsPath=gs://ce-demo2/dataflow/311_request_udf.js,\
inputFilePattern=gs://ce-demo2/dataflow/311_request.json,\
outputTable=ce-demo2:bq_demo.311_landing,\
bigQueryLoadingTemporaryDirectory=gs://ce-demo2/dataflow/tmp/
```

11/9
Adding steps above

11/8/2020
From Dataflow docs CONCEPTS section: What is a Template?
Classic template DAG stored in file in GCS. Flex template stored in container in GCR
Template separate dev from execution.
https://cloud.google.com/dataflow/docs/concepts/dataflow-templates?hl=en_US


11/7/2020
https://cloud.google.com/dataflow/docs/guides/templates/provided-batch?hl=en_US#gcstexttobigquery
#JSON is created in gs://cedemo2/dataflow/schema.JSON
#data file csv is in 




# Hypothesis
1. Subscription templates will be stateful by pulling (ack) from existing subscriptions
1.  Topic tepmlates will be stateless because they'll make their own subscription as part of runtime. Perhaps better for testing.
1. The java libraries in github creates JSON configs to pass to Dataflow runner
1. The files stored in the versioned buckets are JSON outputs.


## Dataflow Templates in Google Cloud Docs
https://cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubtobigquery

## Dataflow Java Source in GitHub
https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/master/src/main/java/com/google/cloud/teleport/templates/PubSubToBigQuery.java

## Full Tutorial in GCP Docs
https://cloud.google.com/solutions/performing-etl-from-relational-database-into-bigquery

#TODO Output tables in BQ must exist before running pipeline
#TODO pick raspi data topic in pubsub
#TODO Define Input topic and output table below
- inputTopic	The Pub/Sub input topic to read from, in the format of projects/<project>/topics/<topic>.
- outputTableSpec	The BigQuery output table location, in the format of <my-project>:<my-dataset>.<my-table>
#TODO pick latest template, see instructions at #1 gs://dataflow-templates/VERSION/PubSub_to_BigQuery





# Java Maven

 https://cloud.google.com/dataflow/docs/quickstarts/quickstart-java-maven
 auth command and key in home folder
 - see WorkCount.java in this dir for more info

## Change to reflect your Project, Buckets, Network, [Subnet if not default]
```
mvn -Pdataflow-runner compile exec:java \
      -Dexec.mainClass=org.apache.beam.examples.WordCount \
      -Dexec.args="--project=ce-demo2 \
      --stagingLocation=gs://ce-demo2/dataflow/staging/ \
      --output=gs://ce-demo2/dataflow/output \
      --runner=DataflowRunner \
      --region=us-central1 \
      --network=custom-vpc
      --subnetwork=regions/us-central1/subnetworks/sn-central1"
```