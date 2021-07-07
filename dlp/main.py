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

import sys
from flask import escape

def redact_gcs(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       Calls DLP function redact_image_all_text().

    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    import os


    PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT")
    OUTPUT_BUCKET = "gs://dlp-outbound"


    #print('Event ID: {}'.format(context.event_id))
    #print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    #print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    #print('Updated: {}'.format(event['updated']))

    # Get Image
    pull_cmd = "gsutil cp gs://{}/{} .".format(event['bucket'], event['name'])
    os.system(pull_cmd)

    # Process image for DLP
    out_file = event['name'] + 'out'
    redact_image_all_text(PROJECT, event['name'], out_file)

    # Push result to output bucket
    push_cmd = "gsutil cp {} gs://{}/".format(out_file, OUT_BUCKET)
    os.system(push_cmd)



def redact_image_all_text(
    project, filename, output_filename,
):
    """Uses the Data Loss Prevention API to redact all text in an image.

    Args:
        project: The Google Cloud project id to use as a parent resource.
        filename: The path to the file to inspect.
        output_filename: The path to which the redacted image will be written.

    Returns:
        None; the response from the API is printed to the terminal.
    """
    # Import the client library
    import google.cloud.dlp

    # Instantiate a client.
    dlp = google.cloud.dlp_v2.DlpServiceClient()

    # Construct the image_redaction_configs, indicating to DLP that all text in
    # the input image should be redacted.
    image_redaction_configs = [{"redact_all_text": True}]

    # Construct the byte_item, containing the file's byte data.
    with open(filename, mode="rb") as f:
        byte_item = {"type_": google.cloud.dlp_v2.FileType.IMAGE, "data": f.read()}

    # Convert the project id into a full resource id.
    parent = f"projects/{project}"

    # Call the API.
    response = dlp.redact_image(
        request={
            "parent": parent,
            "image_redaction_configs": image_redaction_configs,
            "byte_item": byte_item,
        }
    )

    # Write out the results.
    with open(output_filename, mode="wb") as f:
        f.write(response.redacted_image)

    print(
        "Wrote {byte_count} to {filename}".format(
            byte_count=len(response.redacted_image), filename=output_filename
        )
    )








# [START functions_http_content]
def hello_content(request):
    """ Responds to an HTTP request using data from the request body parsed
    according to the "content-type" header.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
        if request_json and 'name' in request_json:
            name = request_json['name']
        else:
            raise ValueError("JSON is invalid, or missing a 'name' property")
    elif content_type == 'application/octet-stream':
        name = request.data
    elif content_type == 'text/plain':
        name = request.data
    elif content_type == 'application/x-www-form-urlencoded':
        name = request.form.get('name')
    else:
        raise ValueError("Unknown content type: {}".format(content_type))
    return 'Hello {}!'.format(escape(name))
# [END functions_http_content]


# [START functions_http_method]
def hello_method(request):
    """ Responds to a GET request with "Hello world!". Forbids a PUT request.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    from flask import abort

    if request.method == 'GET':
        return 'Hello World!'
    elif request.method == 'PUT':
        return abort(403)
    else:
        return abort(405)
# [END functions_http_method]


def hello_error_1(request):
    # [START functions_helloworld_error]
    # This WILL be reported to Stackdriver Error
    # Reporting, and WILL NOT show up in logs or
    # terminate the function.
    from google.cloud import error_reporting
    client = error_reporting.Client()

    try:
        raise RuntimeError('I failed you')
    except RuntimeError:
        client.report_exception()

    # This WILL be reported to Stackdriver Error Reporting,
    # and WILL terminate the function
    raise RuntimeError('I failed you')

    # [END functions_helloworld_error]


def hello_error_2(request):
    # [START functions_helloworld_error]
    # These errors WILL NOT be reported to Stackdriver
    # Error Reporting, but will show up in logs.
    import logging
    print(RuntimeError('I failed you (print to stdout)'))
    logging.warn(RuntimeError('I failed you (logging.warn)'))
    logging.error(RuntimeError('I failed you (logging.error)'))
    sys.stderr.write('I failed you (sys.stderr.write)\n')

    # This is considered a successful execution and WILL NOT be reported to
    # Stackdriver Error Reporting, but the status code (500) WILL be logged.
    from flask import abort
    return abort(500)
    # [END functions_helloworld_error]
