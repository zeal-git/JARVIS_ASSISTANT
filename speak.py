*/speech/speak.py/*

import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
    
if __name__ == "__main__":
    speak("Hello Zeal. I am Jarvis.")
