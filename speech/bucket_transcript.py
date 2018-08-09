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
        print ("=================================")

        pub_url = i.public_url
        gs_link = pub_url.replace("https://storage.googleapis.com/", "gs://")
        print(gs_link)
        operation = speech_recognize.speech_recognize(gs_link)
        print (operation)

        # write results to bucket
        # file = open (i+'transcript', 'xw')
        # file.write(operation.transcript)
        # st_client.writeBlob(srcBucket)


if __name__ == "__main__":
    bucket_recognize(argv[1], argv[2])