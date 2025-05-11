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
    name = input("\n" + "-" * 87 + "\n> ")
    character["name"] = name
    say("-" * 87 + "\n")
    time.sleep(1)
    
    # Ask background
    read_lines(dialog["intro"]["ask_background"], character)

    bg_choice = multiple_choice(
        A="A:  Wandering Orphan",
        B="B:  Forest Child",
        C="C:  Noble Dropout   ",
        D="D:  Quiet Scholar"
    )
    bg_map = {
        "A": "Orphan",
        "B": "Forest",
        "C": "Noble",
        "D": "Scholar"   
    }
    # Set background to bg_map value
    key = bg_choice.strip()[0] 
    character["background"] = bg_map.get(key)
    time.sleep(1)
    
    # Background specific reply
    say(dialog["intro"]["backgrounds"][character["background"]].format(name=character["name"]), 3)
 
    # Ask traits
    read_lines(dialog["intro"]["ask_traits"])
    
    trait_choice = multiple_choice(
        A="A:  Confident, decisive, and inspiring.",
        B="B:  Compassionate, nurturing, and selfless.",
        C="C:  Bold, independent, and disruptive.",
        D="D:  Analytical, wise, and strategic."
    )
    trait_map  = {
        "A": "confident",
        "B": "compassionate",
        "C": "bold",
        "D": "analytical"
    }
    key = trait_choice.strip()[0]
    character["traits"] = trait_map.get(key)

    time.sleep(1)
    
    # Trait specific reply
    read_lines(dialog["trait_response"])
    say(dialog["traits"][character["background"]][character["traits"]].format(name=name), 4)

    return character
