import os
from sys import argv

def convert_to_wav(source_path):
    import ffmpy


    for i in os.listdir(source_path):
        if i.endswith('.wav'):
            ff = ffmpy.FFmpeg(
                inputs={i: None},
                # ac audio channels, ar sampling rate [44100]
                outputs={'output.wav': '-ac 1'}
                )
            ff.run()
            print(i)

if __name__ == "__main__":
    convert_to_wav(argv[1])