import speech_recognition as sr
import os
from pocketsphinx import LiveSpeech, get_model_path
import kural


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



def google_listen():
    # enter the name of usb microphone that you found
    # using lsusb
    # the following name is only used as an example
    mic_name = "Microphone (Realtek High Defini"
    # Sample rate is how often values are recorded
    sample_rate = 48000
    # Chunk is like a buffer. It stores 2048 samples (bytes of data)
    # here.
    # it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    # Initialize the recognizer
    r = sr.Recognizer()

    # generate a list of all audio cards/microphones
    mic_list = sr.Microphone.list_microphone_names()

    # the following loop aims to set the device ID of the mic that
    # we specifically want to use to avoid ambiguity.
    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id =i

    # use the microphone as source for input. Here, we also specify
    # which device ID to specifically look for incase the microphone
    # is not working, an error will pop up saying "device_id undefined"
    with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        kural.green_voice("Hello Shan!, How can I help you?")
        print("listening")
        # listens for the user's input
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            out=("you said: " + text)
            kural.green_voice(out)

        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            out=("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            out=("Could not request results from Google Speech Recognition service;{0}".format(e))

    return out

print(google_listen())
