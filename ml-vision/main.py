# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
"""
EAC NOTES
 - Set config
 - See SLP for outbound bucket info
  gcloud functions deploy redact_gcs --region us-central1 --service-account \
        <svc@account.com> --trigger-bucket dlp-inbound --runtime python38

https://cloud.google.com/functions/docs/calling/storage
"""


from google.cloud import storage
from google.cloud import vision



def sort_faces_gcs(event, context):
    """Pull image, detect faces, sort to default or face bucket"""

    # CONFIG
    project = 'sc-nlp'
    # inbound bucket in deploy call
    # default is destination_bucket with no face, quarantine is pictures with faces
    destination_bucket = "no_face_detected"
    quarantine_bucket = "face_detected"
    output_filename = event['name']

    # CLIENT(s)
    storage_client = storage.Client()
    # leaving in function for testing
    #vision_client = vision.ImageAnnotatorClient()


    # Pull Image
    image = get_face_bytes(storage_client, event['name'], event['bucket'])

    # Detect Faces
    result = detect_faces(vision_client, project, image)

    #TODO Select destination based on result
    if result == True :
        output_bucket_obj = storage_client.get_bucket(quarantine_bucket)
    else :
        output_bucket_obj = storage_client.get_bucket(destination_bucket)
    output_blob = output_bucket_obj.blob(output_filename)

    # Upload image to proper destination
    output_blob.upload_from_string(image)



def get_face_bytes(client, name, bucket):
    """Get image bytes from GCS"""

    # Construct buckets and blobs
    input_bucket_obj = client.get_bucket(bucket)
    input_byte_obj = input_bucket_obj.get_blob()
    
    return input_byte_obj.download_as_bytes()


def detect_faces(image):
    """Take bytes image and detect if faces are present"""
    vision_client = vision.ImageAnnotatorClient()
    
    # Construct the vision config for faces
    image = vision.Image(content = image)
    #features = vision.Feature(1)

    #request = vision.AnnotateImageRequest(
    #    image=image, 
    #    features=features
    #)

    # Call Vision API
 #   response = vision_client.batch_annotate_images(request=request)
    response = vision_client.face_detection(image=image)


    # Parse and return response bytes
    print(response)
    vision_result = response  #TODO what is response format?
    # Bool 
    return vision_result

#For testing 
if __name__ == "__main__":
    with open("faces_and_car.jpg", "rb") as f:
        image = f.read()
    detect_faces(image)