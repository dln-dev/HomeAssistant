import speech_recognition as sr
#import pyttsx3
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
#engine = pyttsx3.init()
#voices = enginge.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

#def talk(text):
#    engine.say(text)
#    enginge.runAndWait()

def execute_command(command):
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
    
    except:
        print("fail")
        command = "error"

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


cont = True

while cont:
    cont = run_jarvis()

print("quit gracefully")
