import time, json
from core.utils import *

def create_character():
    # Import dialog
    with open("data/dialog.json", "r") as file:
        dialog = json.load(file)
    # Init char dictionary
    character = {"rep": 0, "gold": 0}

    # Read intro
    read_lines(dialog["intro"]["hello_world"])
    
    # Prompt name
    name = input("\n" + "-" * 67 + "\n> ")
    character["name"] = name
    say("-" * 67 + "\n")
    time.sleep(1)
    
    # Ask background
    read_lines(dialog["intro"]["ask_background"], character)

    character["background"] = multiple_choice(
        A="Orphan",
        B="Forest",
        C="Noble",
        D="Scholar"
    )
    time.sleep(1)
    
    # Background specific reply
    say(dialog["intro"]["backgrounds"][character["background"]].format(name=character["name"]), 3)
    
    # Ask traits
    read_lines(dialog["intro"]["ask_traits"])

    character["traits"] = multiple_choice(
        A=["confident", "decisive", "inspiring"],
        B=["compassionate", "nurturing", "selfless"],
        C=["bold", "independent", "disruptive"],
        D=["analytical", "wise","strategic"]
    )
    time.sleep(1)
    
    # Trait specific reply
    read_lines(dialog["trait_response"])
    say(dialog["traits"][character["background"]][character["traits"][0]].format(name=name), 4)

    return character
