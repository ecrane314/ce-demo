from google.cloud import storage
import speechRecognize


def bucketRecognize(srcBucket, srcPrefix):
    
    stclient = storage.Client()

    # bucket object iterator
    bucket  = stclient.get_bucket(srcBucket)
    bucketIter = bucket.list_blobs(prefix=srcPrefix)

    for i in bucketIter:

        # speech RecognitionAudio
        link = i.self_link
        rec_audio = speech.types.RecognitionAudio(uri=link)
        operation = spclient.recognize(config=rec_config, audio=rec_audio)

        # write results to bucket
        file = open (i+'transcript', 'xw')
        file.write(operation.transcript)
        stclient.writeBlob(srcBucket)

