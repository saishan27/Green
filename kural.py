import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def check_voice():
    for voice in voices:
        print(voice)
        print("\n")
        x = int(input("Enter index no of voice which u want\n"))
        engine.setProperty('voice' , voices[x].id)
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
