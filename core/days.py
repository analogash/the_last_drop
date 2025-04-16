import json
from core.utils import say, narrate, multiple_choice

def day_zero(character):
    with open("data/dialog.json", "r") as file_1, open("data/actions.json", "r") as file_2:
        dialog = json.load(file_1)
        actions = json.load(file_2)

    say(dialog["day_zero"]["intro"].format(name=character["name"]), 3)
    say(dialog["day_zero"]["lets_go"], 1)
    say("..." + "\033[F", 2)
    say(dialog["day_zero"]["go_get"], 3)
    
    counter = 0
    look_list = actions["intro_look"][character["background"]]

    while True:
        say(dialog["day_zero"]["1st_choice"][0])
        say(dialog["day_zero"]["1st_choice"][1])
        choice_1 = multiple_choice(A="look", B="go")

        if choice_1 == "look":
            narrate(look_list[counter], 3)
            counter = (counter + 1) % len(look_list)

        if choice_1 == "go":
            narrate(actions["intro_go"][character["background"]])
            break






    #print(f"DEBUG: {choice_1}")