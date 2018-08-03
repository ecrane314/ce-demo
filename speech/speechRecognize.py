from google.cloud import speech 
from sys import argv

# 16000 is ideal, 8000 for phone audio
_SAMPLE_RATE=16000


def speechRecognize(source_audio):

    # instantiate clients
    spclient = speech.SpeechClient()
    
    # speech RecognitionConfig
    rec_config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = _SAMPLE_RATE,
    language_code='en-US',
    # max_alternatives, # Not using but available (0-30)
    profanity_filter=True,
    # use_enhanced=True, # Enhanced models  DEPRECATED
    # model='phone_call', # Choose an enhanced model DEPRECATED
    # enable_word_time_offsets=TRUE,  # provide time offsets
    )                


    # source recognition operation
    operation = spclient.recognize(config=rec_config, audio=source_audio)
    return operation


if __name__=="__main__":
    print("argv[1] is: "+argv[1])
    print("argv[1] is type: "+ str(type(argv[1])))
    print("SHOULD NOT SEE THIS, THIS IS -__main__")
    speechRecognize(argv[1])
