import speech_recognition as sr
from settings import DEBUG

listener = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print("in with" if DEBUG else None) 
            listener.adjust_for_ambient_noise(source)
            print("noise adjusted" if DEBUG else None)
            voice = listener.listen(source)
            print("listened" if DEBUG else None)
            command = listener.recognize_google(voice)
            print("recognized" if DEBUG else None)
            command = command.lower()
            print(command if DEBUG else None)
    
    except Exception as e:
        command = "I'm sorry, I did not understand that"
        print(command)
        print("Error: ", e)

    return command


