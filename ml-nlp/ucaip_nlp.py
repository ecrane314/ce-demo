#!/usr/bin/env python3

"""
https://cloud.google.com/ai-platform-unified/docs/tutorials/text-classification-automl
Config in ~/.config/ce-demo
"""

#Prep
#BUCKET=${PROJECT_ID}-lcm
#gsutil mb -p ${PROJECT_ID} -l us-central1 gs://${BUCKET}/
#gsutil -m cp -R gs://cloud-ml-data/NL-classification/happiness.csv gs://${BUCKET}/text/


import json
import os

in_file_path = os.getenv('sample1')
outfile = "scratch.txt"

with open(in_file_path, "r") as gssample:
    call = json.load(gssample)
    print(type(call))

    output = open(outfile,'a')
    #CAUTION: Be careful sorting if multiple calls per file, using false
    #output.write(json.dumps(call, indent=4, sort_keys=False))
    output.close()

    transcript = call['transcript']['transcript'][1:2]  #[pretty_transcript]
    print("=====TRANSCRIPT=====" + str(transcript))

    topics = call.topics
    print(topics)
