import speech_recognition as sr
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

# general setup
owner = "Chewbacca"

phrases = 

listener = sr.Recognizer()
#engine = pyttsx3.init() #'sapi5' for MS
#voices = enginge.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

#def speak(text):
#    engine.say(text)
#    enginge.runAndWait()

def check_if_in_command(phrases, command):
    match = next((phrase for phrase in phrases if phrase in command), False)

    return match


def execute_command(command):
    match = next((phrase for phrase in phrases if phrase in command), False)

    if 'play' in command:
        command = command.replace("play", "")
        print("playing " + command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M") #%I:%M %p
        print(time)

    elif 'kill' in command:
        command = command.replace("kill", "")
        print("os. killal " + command)

    elif 'wikipedia' in command:
        command = command.replace("wikipedia", "")
        info = wikipedia.summary(command, 1)
        print(info)

    elif 'who is' in command:
        command = command.replace("who is", "")
        info = wikipedia.summary(command, 1)
        print(info)

    elif 'tell me about' in command:
        command = command.replace('tell me about', "")
        info = wikipedia.summary(command, 3)
        print(info)

    elif 'joke' in command:
        print(pyjokes.get_joke())

    elif 'say hello to' in command:
        sayHello(command.replace("say hello to", ""))

    else:
        print("I'm sorry, I did not understand that command")


def take_command():
    try:
        with sr.Microphone() as source:
            print("with")
            listener.adjust_for_ambient_noise(source)
            print("noise")
            voice = listener.listen(source)
            print("listened")
            command = listener.recognize_google(voice)
            print("recognized")
            command = command.lower()
            print(command)
    
    except Exception as e:
        command = "I'm sorry, I did not understand that"
        print(command)
        print("Error: ", e)

    return command


def run_jarvis():
    command = take_command()

    if 'quit' in command:
        return False

    elif 'jarvis' in command:
        print("That is my name")
        command = command.replace("jarvis", "")
        execute_command(command)

    return True


def sayHello(name):
    hour = datetime.datetime.now().hour
    helloString = "Hello " + name + ", "

    if hour >= 0 and hour < 12:
        helloString += "good morning"
    elif hour >= 12 and hour < 18:
        helloString += "good afternoon"
    else:
        helloString += "good evening"

    print(helloString)


cont = True

print("Starting up...")
sayHello(owner)

while cont:
    cont = run_jarvis()

print("quit gracefully")
