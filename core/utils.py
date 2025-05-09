import time
import os
import platform

# Say the thing 
def say(text, delay=0):
    print(text)
    time.sleep(delay)

# Say the thing  * with style *
def narrate(text, delay=0):
    width = 67
    lines = text.split("\n")

    for line in lines:
        centered_line = line.center(width)
        print(f"\033[3m{centered_line}\033[0m")

    time.sleep(delay)


def clear_terminal():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


# Takes in options and returns choice
# TODO: Print options here, remove and move options dynamically.
def multiple_choice(**options):
    valid_choices = {key.upper(): value for key, value in options.items()}
    while True:
        say("\n" + "-" * 67)
        choice = input("> ").strip().upper()
        say("-" * 67 + "\n")

        if choice in valid_choices:
            return valid_choices[choice]
        else:

            say("A curious choice... but not valid. Pick one of the available options.", 0)

# Cycles through a dialog section
def read_lines(key, character=None):
    for line in key:
        text = line["text"]
        #  Use player name
        if character and "name" in character:
            text = text.replace("{name}", character["name"])    
        if line["type"] == "say":
            say(text, line["delay"]) 
        if line["type"] == "narrate":
            narrate(text, line["delay"])
