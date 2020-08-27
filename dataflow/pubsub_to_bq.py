#https://cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubtobigquery

#https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/master/src/main/java/com/google/cloud/teleport/templates/PubSubToBigQuery.java

import google

#TODO Input topic and output table
#inputTopic	The Pub/Sub input topic to read from, in the format of projects/<project>/topics/<topic>.
#outputTableSpec	The BigQuery output table location, in the format of <my-project>:<my-dataset>.<my-table>