"""
Pull and push object from Google cloud storage buckets

"""
from google.cloud import storage

# CONFIG
SOURCE_BUCKET = 'dlp-outbound'
DEST_BUCKET = 'dlp-outbound'

# COMMON CLIENT
client = storage.Client()

def pull_obj():
    """Copy a cloud bucket object to local variable"""
    # Construct bucket and blob objects
    bucket_obj = client.get_bucket(SOURCE_BUCKET)
    blob = bucket_obj.get_blob("VIN4.jpeg")

    # Download blob and write to file
    pic = blob.download_as_bytes()
    with open("scratch.jpg", 'wb') as f:
        f.write(pic)


def push_obj():
    """Create a local object and upload to bucket"""
    # Construct bucket and new blob
    bucket_obj = client.get_bucket(DEST_BUCKET)
    lor_blob = bucket_obj.blob("lorem_gcs.txt")

    with open("lorem.txt", "rb") as f:
        #text_bytes = f.read()
        lor_blob.upload_from_file(f)

if __name__ == "__main__":
    #pull_obj()
    push_obj()