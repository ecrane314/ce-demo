from google.cloud import storage
import speechRecognize


def bucketRecognize(srcBucket, srcPrefix):

    # storage client
    stclient = storage.Client()

    # bucket and object iterator
    bucket  = stclient.get_bucket(srcBucket)
    bucketIter = bucket.list_blobs(prefix=srcPrefix)

    for i in bucketIter:

        # speech RecognitionAudio
        link = i.self_link
        rec_audio = speech.types.RecognitionAudio(uri=link)
        operation = speechRecognize(rec_audio)
        
        print(operation)
        # write results to bucketv
      #  file = open (i+'transcript', 'xw')
       # file.write(operation.transcript)
       # stclient.writeBlob(srcBucket)

