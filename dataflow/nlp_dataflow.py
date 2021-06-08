"""
NLP via DataFlow -- Lak's original here...
https://gist.github.com/lakshmanok/a07d488a0b8006c26bdee0a7effd6245
Added comments, 
updated deprecated items,
more focus on configuration

Formats used:
| 'dataflow ui title' >> command

Note: imports, functions and other variables defined in the global context
of your __main__ file of your Dataflow pipeline are, by default, not available
in the worker execution environment, and such references will cause a
NameError, unless the --save_main_session pipeline option is set to True.
Please see https://cloud.google.com/dataflow/faq#how-do-i-handle-nameerrors for
additional documentation on configuring your worker execution environment.
"""


from datetime import datetime
import apache_beam as beam


PROJECT='sc-nlp'
BUCKET='sc-nlp-x'
REGION='us-central1'
#TODO add table to write results DEST_TABLE=''


def parse_nlp_result(response):
    return [
        # response, # entire string
        response.sentences[0].text.content,
        response.language,
        response.document_sentiment.score
        # Added to include entities
        # response.entities[0]
    ]

def run():
    # Leave imports here so gets pickled and goes to workers
    from apache_beam.ml.gcp import naturallanguageml as nlp
    # https://beam.apache.org/releases/pydoc/2.29.0/apache_beam.ml.gcp.naturallanguageml.html


#TODO   Natural Language API reference. Does Beam call this?
    # https://googleapis.dev/python/language/latest/usage.html

    # Configuration for AnnotateText request
    features_requested = nlp.types.AnnotateTextRequest.Features(
            extract_entities=True,
            extract_document_sentiment=True,
            extract_syntax=False
        )
    bq_source_query = "SELECT text FROM `bigquery-public-data.hacker_news.comments` WHERE author = 'AF' AND LENGTH(text) > 10"


    # Contruct Beam pipeline, view as Dataflow Pipeline, assign options
    options = beam.options.pipeline_options.PipelineOptions()
    google_cloud_options = options.view_as(beam.options.pipeline_options.GoogleCloudOptions)
    google_cloud_options.project = PROJECT
    google_cloud_options.region = REGION
    google_cloud_options.job_name = 'nlpapi-{}'.format(datetime.now().strftime("%Y%m%d-%H%M%S"))
    google_cloud_options.staging_location = 'gs://{}/staging'.format(BUCKET)
    google_cloud_options.temp_location = 'gs://{}/temp'.format(BUCKET)


    # Assign DataflowRunner as runner for pipeline, required as includes auth flow
    options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'DataflowRunner' # 'DirectRunner'
    

    # Pipeline
    p = beam.Pipeline(options=options)
    (p 
    #   BigQuerySource is deprecated since 2.25.0. Use ReadFromBigQuery instead.
     #| 'bigquery' >> beam.io.Read(beam.io.BigQuerySource(
     #    query=bq_source_query,
     #    use_standard_sql=True))
      | 'Read bq'  >> beam.io.ReadFromBigQuery(
          query=bq_source_query,
          use_standard_sql=True)
      | 'txt'      >> beam.Map(lambda x : x['text'])
      | 'doc'      >> beam.Map(lambda x : nlp.Document(x, type='PLAIN_TEXT'))
    #  | 'todict'   >> beam.Map(lambda x : nlp.Document.to_dict(x))
      | 'nlp'      >> nlp.AnnotateText(features_requested, timeout=10)
      | 'parse'    >> beam.Map(parse_nlp_result)
      | 'gcs'      >> beam.io.WriteToText('gs://{}/output2.txt'.format(BUCKET), num_shards=1)
#TODO   | 'write to bq'  >> beam.io.WriteToBigQuery()
    )
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    run()