from sys import argv
import speech_recognize


def bucket_recognize(src_bucket, src_prefix):
    """Take a bucket and prefix and return transcript by calling
    speech_recognize"""

    # storage client
    from google.cloud import storage
    st_client = storage.Client()

    # bucket and object iterator
    bucket = st_client.get_bucket(src_bucket)
    bucket_iter = bucket.list_blobs(prefix=src_prefix)

    for i in bucket_iter:

        # speech RecognitionAudio
        print"================================="

        try:
            gs_link = "gs://" + src_bucket + src_prefix + i.
            operation = speech_recognize.speech_recognize(gs_link)
            print operation
        except:
            print "Not a WAV, skipping"


        # try:
        #     operation = speech_recognize.speech_recognize(i.self_link)
        #     print operation
        # except:
        #     print "Not i.self_link"
        #
        # try:
        #     operation2 = speech_recognize.speech_recognize(i.path)
        #     print operation2
        # except:
        #     print "Not i.path"
        #
        # try:
        #     operation3 = speech_recognize.speech_recognize(i.public_url)
        #     print operation3
        # except:
        #     print "Not i.public_url"
        #
        # try:
        #     operation4 = speech_recognize.speech_recognize(i.media_link)
        #     print operation4
        # except:
        #     print "Not i.media_link"


        break  # remove once working

        # write results to bucket
        # file = open (i+'transcript', 'xw')
        # file.write(operation.transcript)
        # st_client.writeBlob(srcBucket)


if __name__ == "__main__":
    print "argv[1] is type: "+ str(type(argv[1])) + argv[1]
    bucket_recognize(argv[1], argv[2])