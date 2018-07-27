#!/bin/python3
from google.cloud import speech, storage
from sys import argv

def sttAlpha(srcBucket, srcPrefix, destPrefix):
	
	# clients
	spclient = speech.SpeechClient()
        stclient = storage.Client()
    
        #speech config
	config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code='en-US',
        profanity_filter=True,
        
        # Enhanced models require opt in for audio data collection
        use_enhanced=True,
    	# A model must be specified to use enhanced model.
        model='phone_call')
    
    #bucket object iterator
 	bucket  = stclient.get_bucket(srcBucket)
 	bucketIter = bucket.list_blobs()

    for i in bucketIter:
    	#cycle audio and run recognition
    	audio = speech.types.RecognitionAudio(i)
	    operation = spclient.long_running_recognize(config, audio)
		
		#write results to bucket
		file = open (i+'script-enh', 'wx')
		file.write(operation.transcript)
		stclient.writeBlob(target bucket)
		

if __name__=="__main__":
	sttAlpha(argv[1], argv[2], argv[3])
