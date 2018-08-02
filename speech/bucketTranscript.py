from google.cloud import storage
import speechRecognize
from sys import argv

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


if __name__=="__main__":
    print("argv[1] is: "+argv[1])
    print("argv[1] is type: "+ str(type(argv[1])))
    print("SHOULD SEE THIS, THIS IS -__main__")
    bucketRecognize(argv[1], argv[2])
