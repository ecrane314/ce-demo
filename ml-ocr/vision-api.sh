#!/usr/bin/env bash

# 1 https://google.qwiklabs.com/focuses/9369
# 2 export API_KEY before beginning
# 3 modify ocr-req to point to your image

curl -s -X POST -H "Content-Type: application/json" --data-binary @ocr-req.json \  
https://vision.googleapis.com/v1/images:annotate?key=${API_KEY} -o ocr-out.json
