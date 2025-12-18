#!/env bash

MODEL_ID="gemini-3-flash-preview"
PROJECT_ID="ce-demo1"
REGIONS=["us-central1","us-east4","europe-west4"]


curl \
  -X POST \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  -H "x-client-request-id: 2037622167" \
  -H "Content-Type: application/json" \
  https://aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGIONS[0]}/publishers/google/models/${MODEL_ID}:streamGenerateContent -d \
  $'{
    "contents": {
      "role": "user",
      "parts": [
        {
          "text": "Describe the most recently launched version of Gemini in 1 sentence"
        }
      ]
    }
  }'