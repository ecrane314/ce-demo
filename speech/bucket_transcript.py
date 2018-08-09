from sys import argv
from google.cloud import storage
import speech_recognize


def bucket_recognize(src_bucket, src_prefix):
    """Take a bucket and prefix and return transcript by calling
    speech_recognize"""

    # storage client
    st_client = storage.Client()

    # bucket and object iterator
    bucket = st_client.get_bucket(src_bucket)
    bucket_iter = bucket.list_blobs(prefix=src_prefix)

    for i in bucket_iter:

        # speech RecognitionAudio
        print"================================="

        operation = speech_recognize.speech_recognize(i.self_link)
        operation2 = speech_recognize.speech_recognize(i.path)
        operation3 = speech_recognize.speech_recognize(i.public_url)
        operation4 = speech_recognize.speech_recognize(i.media_link)

        print operation
        print operation2
        print operation3
        print operation4
        break  # remove once working

        # write results to bucket
        # file = open (i+'transcript', 'xw')
        # file.write(operation.transcript)
        # st_client.writeBlob(srcBucket)


if __name__ == "__main__":
    print "argv[1] is: "+argv[1]
    print "argv[1] is type: "+ str(type(argv[1]))
    print "SHOULD SEE THIS, THIS IS -__main__"
    bucket_recognize(argv[1], argv[2])