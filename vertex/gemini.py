#!/usr/bin/env python

import os
import subprocess
import uuid
import requests
import json

MODEL_ID = "gemini-2.5-flash"
PROJECT_ID = "ce-demo1"
REGIONS = ["us-central1", "europe-west4", "asia-south1"]


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

token = get_gcloud_token()

if token:
    for region in REGIONS:
        print(f"--- Querying Gemini in {region} ---")
        url = f"https://{region}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{region}/publishers/google/models/{MODEL_ID}:streamGenerateContent"
        
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
