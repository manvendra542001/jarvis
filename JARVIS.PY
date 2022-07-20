from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("GOOD MORNING!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening ")
    speak("HELLO I AM JARVIS A AI DEVLOPED BY MANVENDRA SINGH HOW MAY I HELP YOU")       
#takes microphone input and gives out string output             
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is ready to take commands please say something to the microphone")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query= r.recognize_google(audio, Language="en-in") 
        print(f"user said:{query}\n")
    except Exception as e:
       # print(e)
        print("Say that again please")
        return "None"
    return query
        
if __name__=="__main__":
   # speak("HELO DADU BHIYA ABHI SO RAHE HA
   wishme()
#    speak("Hello snapchat i am jarvis ai devloped by manvendra singh")
   takecommand()