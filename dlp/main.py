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
 - On deploy, set service account if needed for permissions
 - On deploy, gcfunction name must match entry function from source
 - Build source will be zipped and copied as is to a GCS bucket
 - Function build artifacts will live in separate bucket
  gcloud functions deploy redact_gcs --region us-central1 --service-account \
        <svc@account.com> --trigger-bucket dlp-inbound --runtime python38
"""


from google.cloud import storage
from google.cloud import dlp_v2


def redact_gcs(event, context):
    """Pull image, redact, push image using client libraries"""
    # CLIENT
    storage_client = storage.Client()

    # CONFIG
    # NOTE  project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    # ENV variable only exists in GCE, not GCF runtime
    project = 'sc-nlp'
    destination_bucket = "dlp-outbound"  # inbound bucket is in deploy call
    output_filename = event['name']

    # Construct buckets and blobs
    input_bucket_obj = storage_client.get_bucket(event['bucket'])
    input_byte_obj = input_bucket_obj.get_blob(event['name'])    #['selfLink']
    input_bytes = input_byte_obj.download_as_bytes()

    output_bucket_obj = storage_client.get_bucket(destination_bucket)
    output_blob = output_bucket_obj.blob(output_filename)

    # Write bytes to object and upload
    result = redact_image_all_text(project, input_bytes)
    output_blob.upload_from_string(result)


def redact_image_all_text(project, input_bytes):
    """Take byets image and redact all tax"""
    # Construct client
    dlp_client = dlp_v2.DlpServiceClient()

    # Construct the image_redaction_config,
    # Indicating DLP should redact all text
    parent = f"projects/{project}"
    image_redaction_configs = [{"redact_all_text": True}]
    byte_item = {"type_": dlp_v2.FileType.IMAGE, "data": input_bytes}

    # Call DLP API
    response = dlp_client.redact_image(
        request={
            "parent": parent,
            "image_redaction_configs": image_redaction_configs,
            "byte_item": byte_item,
        }
    )

    # Parse and return response bytes
    redacted_bytes = response.redacted_image
    return redacted_bytes
