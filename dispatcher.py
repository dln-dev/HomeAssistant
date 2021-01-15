# implement functionality
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
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# get implemented phrases
from phrases import phrases, PHRASES

# for debugging
from settings import DEBUG, SPEAKER, PRINT, VOICE, NEWS_URL, FESTIVAL

# gets the wolfram alpha app id
from secrets import WA_ID


if SPEAKER:
    if FESTIVAL:
        import os

        def speak(text):
            speech = "festival -b '(voice_cmu_us_slt_arctic_hts)' \
                       '(SayText \"" + text + "\")'"

            os.system(speech)

    else:
        import pyttsx3
        engine = pyttsx3.init() #'sapi5' for MS
        voices = engine.getProperty('voices')
        # linux uses espeak, voices are meh
        engine.setProperty('voice', voices[10].id) #0 if voice == "male" else 1].id)
    
        def speak(text):
            engine.say(text)
            engine.runAndWait()



def execute_command(command):
    match = next((phrase for phrase in PHRASES if phrase in command), "")
    command = output(command=command, match=match, play=False)

    if check_match(match, "music_phrases"): 
        output("playing", command, "now")
        print("playing " + command)

    elif check_match(match, "time_phrases"):
        time = datetime.datetime.now().strftime("%H:%M") #%I:%M %p
        output("the current time is", time)

    elif check_match(match, "close_phrases"):
        output("closing", command, "now")
        print("os. killal " + command)

    elif check_match(match, "wiki_phrases"):
        output("searching wikipedia for", command)
        info = wikipedia.summary(command, 3)
        output(command=info)

    elif check_match(match, "info_phrases"):
        output("searching wikipedia for information about", command)
        info = wikipedia.summary(command, 1)
        output(command=info)

    elif check_match(match, "joke_phrases"):
        output(command=pyjokes.get_joke())

    elif check_match(match, "hello_phrases"):
        sayHello(command)

    elif check_match(match, "news_phrases"):
        with urlopen(NEWS_URL) as client:
            xml_page = client.read()
        
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item", limit=3)
        
        for i,news in enumerate(news_list):
            output(str(i+1), news.title.text)

    elif check_match(match, "alpha_phrases"):
        client = wolframalpha.Client(WA_ID)
        try:
            received = client.query(command)
            answer = next(received.results).text
            output("wolfram alpha says", answer)
        except Exception as e:
            output(command="WA failure in :"+command+" Exception:" + str(e))
            output("wolfram alpha cannot handle this question")
 
    elif check_match(match, "reboot_phrases"):
        output("I will reboot in 10 seconds")
        #subprocess.call(["reboot", "now"])

    elif match == "":
        pass

    else:
        output("I'm sorry, I did not understand that command")


def check_match(match, kind):
    return any(p in match for p in phrases[kind])


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



