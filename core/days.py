import json
from core.utils import *

def day_zero(character):
    with open("data/dialog.json", "r") as file:
        dialog = json.load(file)
    
    read_lines(dialog["zero_intro"], character)

    counter = 0
    look_list = dialog["intro_look"][character["background"]]

    while True:
        say(dialog["1st_choice"][0])
        say(dialog["1st_choice"][1])
        choice_1 = multiple_choice(A="look", B="go")

        if choice_1 is "look":
            narrate(look_list[counter]["text"])
            counter = (counter + 1) % len(look_list)

        if choice_1 is "go":
            read_lines(dialog["intro_go"][character["background"]], character)
            break

    while True:
        say(dialog["herb_look_options"][0])
        say(dialog["herb_look_options"][1])

        choice_2 = multiple_choice(A="look", B="collect", C="go")

        if choice_2 is "look":
            narrate(dialog["herbs_look"][character["background"]], 3)

        if choice_2 is "collect":
            read_lines(dialog["herbs_collect"][character["background"]], character)

        if choice_2 is "go":
            break

    #print(f"DEBUG: {choice_1}")
