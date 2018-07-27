#!/bin/python3
from google.cloud import speech, storage
from sys import argv

# 16000 is ideal, 8000 for phone audio
_SAMPLE_RATE=16000


def speechRecognize(srcBucket):
	
    # instantiate clients
    spclient = speech.SpeechClient()
    stclient = storage.Client()
    
    # speech RecognitionConfig
    config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = _SAMPLE_RATE,
    language_code='en-US',
    # max_alternatives, # Not using but available (0-30)
    profanity_filter=True,
    # use_enhanced=True, # Enhanced models  DEPRECATED
    # model='phone_call', # Choose an enhanced model DEPRECATED
    # enable_word_time_offsets=TRUE,  # provide time offsets
    ) 

    # bucket object iterator
    bucket  = stclient.get_bucket(srcBucket)
    bucketIter = bucket.list_blobs()

    for i in bucketIter:
        
        # speech RecognitionAudio
        audio = speech.types.RecognitionAudio(content=i)
        operation = spclient.recognize(config, audio)

        # write results to bucket
        file = open (i+'transcript', 'xw')
        file.write(operation.transcript)
        stclient.writeBlob(srcBucket)
                

if __name__=="__main__":
	speechRecognize(argv[1])
