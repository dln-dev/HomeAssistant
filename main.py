from listener import listen_for_name, take_command
from dispatcher import execute_command
from settings import NAME, OWNER

def run_jarvis():
    command = input()#take_command()

    if NAME in command:
        command = command.replace(NAME, "")
        execute_command(command)

    return 'quit' in command


quit = False

print("Starting up "+ NAME + "...")

execute_command("say hello to " + OWNER)

while not quit:
    quit = run_jarvis()

print("quit gracefully")
