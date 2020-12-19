from listener import take_command
from dispatcher import execute_command
from settings import owner

def run_jarvis():
    command = take_command()

    if 'jarvis' in command:
        command = command.replace("jarvis", "")
        execute_command(command)

    return not 'quit' in command


cont = True

print("Starting up...")

execute_command("say hello to " + owner)

while cont:
    cont = run_jarvis()

print("quit gracefully")
