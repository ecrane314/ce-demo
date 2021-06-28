"""
Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/

SEED    https://cloud.google.com/text-to-speech/docs/create-audio
PREREQS Enable API 
"""

from google.cloud import texttospeech


# ----------BEGIN CONFIG----------
# Effects profile, like phone call
# https://cloud.google.com/text-to-speech/docs/audio-profiles
FX_PROFILE = 'telephony-class-application'
# https://cloud.google.com/text-to-speech/docs/voices
VOICE = 'en-GB-Wavenet-A'
GENDER = 'MALE'  #FEMALE, MALE, NEUTRAL
#VOICE_SPEED = 
#VOICE_PITCH = 
INPUT_FILE = 'tts-input.txt'  #Longer form and no input in repo
OUTPUT_FILE = 'en-GB-Wavenet-A-Female-IVR.mp3' #Change if updating config
# ----------END CONFIG----------


# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
# synthesis_input = texttospeech.SynthesisInput(text="And Caesar wept, for there were no more worlds to conquer")
with open(INPUT_FILE, 'r') as file:
    file_input = file.read()
synthesis_input = texttospeech.SynthesisInput(text=file_input)


#TODO Move everything from here down to function definition

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    name = VOICE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3, 
    effects_profile_id=[FX_PROFILE]
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(OUTPUT_FILE, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file {}'.format(OUTPUT_FILE))