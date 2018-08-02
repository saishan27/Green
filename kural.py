import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def check_voice():
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say("hello world")
        print("hello wolrd",voice)
        engine.runAndWait()
        engine.stop


def green_voice(out):
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.setProperty('rate',150)
    # engine.setProperty('volume',100)
    engine.say(out)
    engine.runAndWait()
    engine.stop


green_voice("")