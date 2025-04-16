import json
from utils import say, narrate, multiple_choice

def day_zero(character):
    with open("dialog.json", "r") as file_1, open("look.json", "r") as file_2:
        dialog = json.load(file_1)
        look = json.load(file_2)
        
    say(dialog["day_zero"]["intro"].format(name=character["name"]), 2)
    say("\n..." + "\033[F", 2)
    say(dialog["day_zero"]["lets_go"], 1)
    say(dialog["day_zero"]["go_get"], 3)
    say(dialog["day_zero"]["1st_choice"][0])
    say(dialog["day_zero"]["1st_choice"][1])
    choice_1 = multiple_choice(A="look", B="go")

    if choice_1 == "look":
        narrate(look["intro"][character["background"]])

    if choice_1 == "go":
        pass






    #print(f"DEBUG: {choice_1}")