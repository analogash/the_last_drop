import time
import os
import platform

def say(text, delay=0):
    print(text)
    time.sleep(delay)

def narrate(text, delay=0):
    print(f"\033[3m{text}\033[0m")  # Italic-style with ANSI
    time.sleep(delay)

def clear_terminal():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def multiple_choice(**options):
    valid_choices = {key.upper(): value for key, value in options.items()}
    while True:
        say("\n" + "-" * 55)
        choice = input("> ").strip().upper()
        say("-" * 55 + "\n")

        # Validate and return the choice
        if choice in valid_choices:
            return valid_choices[choice]
        else:
            say("A curious choice... but not valid. Pick one of the available options.", 0)
