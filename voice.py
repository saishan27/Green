import speech_recognition as sr
import os
from pocketsphinx import LiveSpeech, get_model_path
import pyaudio

# obtain audio from the microphone
def accurate_voice():
        r = sr.Recognizer()
        with sr.Microphone() as source:
          print("Please wait. Calibrating microphone...")
          # listen for 5 seconds and create the ambient noise energy level
          r.adjust_for_ambient_noise(source, duration=5)
          print("Say something!")
          audio = r.listen(source)

        # recognize speech using Sphinx
        try:
          out = ("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
        except sr.UnknownValueError:
          out = ("Sphinx could not understand audio")
        except sr.RequestError as e:
          out = ("Sphinx error; {0}".format(e))

        return out



# Script 2 - Immediate albeit inaccurate speech-to-text:


def immediate_voice():
    model_path = get_model_path()
    speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'en-us'),
    lm=os.path.join(model_path, 'en-us.lm.bin'),
    dic=os.path.join(model_path, 'cmudict-en-us.dict')
    )
    for phrase in speech: print(phrase)

    return phrase

print(accurate_voice())