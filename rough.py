import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("code to add voice to windows computer")
