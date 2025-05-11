import time
import os
import platform

# Say the thing 
def say(text, delay=0):
    print(text)
    time.sleep(delay)

# Say the thing  * with style *
def narrate(text, delay=0):
    width = 87
    lines = text.split("\n")

    for line in lines:
        centered_line = line.center(width)
        print(f"\033[3m{centered_line}\033[0m")

    time.sleep(delay)


def clear_terminal():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


# Takes in options and returns choice
def multiple_choice(**options):
    valid_choices = {key.upper(): value for key, value in options.items()}
    option_values = list(valid_choices.values())
    def is_long(value): 
        return len(value) > 40

    while True:
        print()
        if any(is_long(v) for v in option_values):
            # Print one per line
            for value in option_values:
                print(value)
        else:
            # Print two per line
            for i in range(0, len(option_values), 2):
                line = option_values[i]
                if i + 1 < len(option_values):
                    line += "    " + option_values[i + 1]
                print(line)

        say("\n" + "-" * 87)
        choice = input("> ").strip().upper()
        say("-" * 87 + "\n")

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
