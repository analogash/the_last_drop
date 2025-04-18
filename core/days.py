import json
from core.utils import *

def day_zero(character):
    with open("data/dialog.json", "r") as file_1, open("data/actions.json", "r") as file_2:
        dialog = json.load(file_1)
        actions = json.load(file_2)
    
    read_lines(character, dialog["zero_intro"], say)

    counter = 0
    look_list = actions["intro_look"][character["background"]]

    while True:
        say(dialog["1st_choice"][0])
        say(dialog["1st_choice"][1])
        choice_1 = multiple_choice(A="look", B="go")

        if choice_1 is "look":
            narrate(look_list[counter], 3)
            counter = (counter + 1) % len(look_list)

        if choice_1 is "go":
            read_lines(character, actions["intro_go"][character["background"]], say)
            break

    while True:
        say(actions["herb_look_options"][0])
        say(actions["herb_look_options"][1])

        choice_2 = multiple_choice(A="look", B="collect", C="go")

        if choice_2 is "look":
            narrate(actions["herbs_look"][character["background"]], 3)

        if choice_2 is "collect":
            read_lines(character, actions["herbs_collect"][character["background"]], say)

        if choice_2 is "go":
            break

    #print(f"DEBUG: {choice_1}")