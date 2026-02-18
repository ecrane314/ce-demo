#!/usr/bin/env python

import os
import subprocess
import uuid
import requests
import json

from google.genai import types
from google import genai

# MODEL_ID = "gemini-2.5-flash-preview-09-2025"
MODEL_ID = "gemini-flash-latest"
PROJECT_ID = "ce-demo1"
# REGIONS = ["us-central1", "europe-west4", "asia-south1"]
REGIONS = [ "global"]


def get_gcloud_token():
    """Gets the gcloud auth token."""
    try:
        token = subprocess.check_output(
            ["gcloud", "auth", "application-default", "print-access-token"], 
            text=True
        ).strip()
        return token
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error getting gcloud token: {e}")
        print("Please ensure 'gcloud' is installed and you are authenticated.")
        return None


def requests_vertex(token):
    for region in REGIONS:
        print(f"--- Querying Gemini in {region} ---")
        # url = f"https://{region}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{region}/publishers/google/models/{MODEL_ID}:streamGenerateContent"
        url = f"https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/publishers/google/models/{MODEL_ID}:streamGenerateContent"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "x-client-request-id": str(uuid.uuid4()),
            "Content-Type": "application/json; charset=utf-8",
        }

        data = {
            "contents": {
                "role": "user",
                "parts": [{"text": "In one sentence, explain vector databases."}]
            }
        }

        response = requests.post(url, headers=headers, json=data, stream=True)

        if response.status_code == 200:
            for chunk in response.iter_content(chunk_size=None):
                # Process each chunk of the streaming response
                print(chunk.decode('utf-8'), end="")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
        print("\n" + "="*40 + "\n")

def vertex_library(token):
    client = genai.Client(
    vertexai=True)

    # If your image is stored in Google Cloud Storage, you can use the from_uri class method to create a Part object.
    IMAGE_URI = "gs://generativeai-downloads/images/scones.jpg"
    model = MODEL_ID
    response = client.models.generate_content(
    model=model,
    contents=[
        "What is shown in this image?",
        types.Part.from_uri(
        file_uri=IMAGE_URI,
        mime_type="image/png",
        ),
    ],
    )
    print(response.text, end="")

if __name__ == "__main__":
    token = get_gcloud_token()
    requests_vertex(token)
    # vertex_library(token)

