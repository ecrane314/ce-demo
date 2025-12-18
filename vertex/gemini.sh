#!/bin/bash

PROJECT="ce-demo1"
REGION="eu"
MODEL_ID="gemini-2.5-flash"


PROMPT_TEXT="Describe Vector databases in one sentence as it relates to LLMs"

curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://${REGION}-aiplatform.googleapis.com/v1/projects/${PROJECT}/locations/${REGION}/publishers/google/models/${MODEL_ID}:streamGenerateContent" \
  -d @- <<EOF
{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "${PROMPT_TEXT}"
    }]
  }]
}
EOF
