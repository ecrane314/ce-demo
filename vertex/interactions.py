from google import genai
import os

api_key = os.getenv('api_key')
client = genai.Client(api_key=api_key)

interaction =  client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)

print(interaction.outputs[-1].text)