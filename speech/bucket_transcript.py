from sys import argv
from google.cloud import storage
import speech_recognize

def bucket_recognize(src_bucket, src_prefix):
    """Take a bucket and prefix and return transcript by calling
    speech_recognize"""

    # storage client
    stclient = storage.Client()

    # bucket and object iterator
    bucket = stclient.get_bucket(src_bucket)
    bucket_iter = bucket.list_blobs(prefix=src_prefix)

    for i in bucket_iter:

        # speech RecognitionAudio
        print i.self_link
        print i.path
        print i.public_url
        print i.media_link
        link = i.self_link
        print"=================================" 
        operation = speech_recognize.speech_recognize(link)

        print operation
        # write results to bucketv
        #  file = open (i+'transcript', 'xw')
       # file.write(operation.transcript)
       # stclient.writeBlob(srcBucket)


if __name__ == "__main__":
    print "argv[1] is: "+argv[1]
    print "argv[1] is type: "+ str(type(argv[1]))
    print "SHOULD SEE THIS, THIS IS -__main__"
    bucket_recognize(argv[1], argv[2])
