# implement functionality
#import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests

# get implemented phrases
from settings import phrases

# for debugging
from settings import DEBUG, SPEAKER, PRINT, VOICE


if SPEAKER:
    engine = pyttsx3.init() #'sapi5' for MS
    voices = enginge.getProperty('voices')
    engine.setProperty('voice', voices[0 if voice == "male" else 1].id)
    
    def speak(text):
        engine.say(text)
        enginge.runAndWait()



def execute_command(command):
    match = next((phrase for phrase in phrases if phrase in command), False)
    command = output(command=command, match=match, play=False)

    if match == 'play': 
        output("playing", command, "now")
        print("playing " + command)

    elif match == 'time' or match == 'clock':
        time = datetime.datetime.now().strftime("%H:%M") #%I:%M %p
        output("the current time is", time)

    elif match == 'kill':
        output("closing", command, "now")
        print("os. killal " + command)

    elif match == 'wikipedia':
        output("searching wikipedia for", command)
        info = wikipedia.summary(command, 1)
        output(command=info)

    elif match == 'who is':
        output("searching wikipedia for information about", command)
        info = wikipedia.summary(command, 1)
        output(command=info)

    elif match == 'tell me about':
        output('looking for information about', command, "on wikipedia...") 
        info = wikipedia.summary(command, 3)
        print(info)

    elif match == 'joke':
        output(command=pyjokes.get_joke())

    elif match == 'say hello to':
        sayHello(command)

    elif match == "":
        pass

    else:
        print("I'm sorry, I did not understand that command")



def sayHello(name):
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        greeting = ", good morning"
    elif hour >= 12 and hour < 18:
        greeting = ", good afternoon"
    else:
        greeting = ", good evening"

    output("Hello", name, greeting)



def output(prefix="", command="", suffix="", match="", play=True):
    if DEBUG:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        with open("DEBUG.log", "a") as debug:
            debug.write(time + " DEBUG: match = " + match + ", command = " + command + "\n")

    command = command.replace(match, "")
    
    if play:
        if SPEAKER:
            speak(prefix + " " + command + " " + suffix)

        if PRINT:
            print(prefix + " " + command + " " + suffix)

    return command



