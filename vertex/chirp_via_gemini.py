
import os
import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "ce-demo1"
MODEL_ID = "gemini-2.5-flash"
LOCATION = "us-central1"

def generate_chirp_instruction():
    print(f"Calling {MODEL_ID} in {LOCATION} for project {PROJECT_ID} using Vertex AI SDK...")
    
    # Initialize Vertex AI
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    
    # Instantiate the model
    model = GenerativeModel(MODEL_ID)

    prompt = "Call Chirp 3 via Vertex AI and instruct it to use a UK voice with wavenet, if available, to say 'Hello, World! It's a lovely day in London' and save the output file in gs://ce-demo1/chirp_output/"

    try:
        response = model.generate_content(prompt)
        print("Response from Gemini:")
        print(response.text)
    except Exception as e:
        print(f"Error calling Gemini: {e}")

if __name__ == "__main__":
    generate_chirp_instruction()
