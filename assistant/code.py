import datetime
import webbrowser
import os
from time import strftime
import pyttsx3
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <= 12:
        speak("good morning robbie")
    elif (hour >= 12 and hour <= 17):
        speak("good afternoon robbie")
    elif (hour >= 17):
        speak("good evening robbie")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        querry = r.recognize_google(audio, language="en-in")
        print("usersaid "+querry)
        return querry
    except Exception as e:
        print("say that again please")
        return "None"


if (__name__ == "__main__"):
    wishme()
    while True:
        querry = takecommand().lower()
        if "wikipedia" in querry:
            speak("searching wikipedia")
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in querry:
            webbrowser.open("youtube.com")

        elif "open google" in querry:
            webbrowser.open("google.com")

