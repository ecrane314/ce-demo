from sys import argv

# 16000 is ideal, 8000 for phone audio
_SAMPLE_RATE=44100


def speech_recognize(source_audio):
    """Take source audio uri and call google-cloud-speech recognize
    method. Return transcript"""

    # instantiate client
    from google.cloud import speech
    sp_client = speech.SpeechClient()
    
    # speech RecognitionConfig
    rec_config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=_SAMPLE_RATE,
        profanity_filter=True,
        language_code='en-US'
        # max_alternatives, # Not using but available (0-30)
        # enable_word_time_offsets=TRUE,  # provide time offsets
    )                

    # speech RecognitionAudio from argument
    rec_audio = speech.types.RecognitionAudio(uri=source_audio)

    # recognition operation
    operation = sp_client.recognize(rec_config, rec_audio)
    return operation


if __name__=="__main__":
    speech_recognize(argv[1])
