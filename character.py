import time, json
from utils import say, multiple_choice

def create_character():
    with open("dialog.json", "r") as file:
        dialog = json.load(file)

    character = {"rep": 0}
    say(dialog["static"]["welcome"])
    say(dialog["static"]["apprentice_intro"], 2)
    say(dialog["static"]["ask_name"], 0)
    name = input("\n> ")
    character["name"] = name
    time.sleep(1)
    
    say(dialog["static"]["hello_name"].format(name=name), 2)
    say(dialog["static"]["scatter_brain"], 2)
    say(dialog["static"]["need_help"], 2)
    say("...\n")
    say(dialog["static"]["ask_background"].format(name=name), 2)
    say(dialog["static"]["background_options"][0], 0)
    say(dialog["static"]["background_options"][1], 0)
    say(dialog["static"]["background_options"][2], 0)
    say(dialog["static"]["background_options"][3], 0)

    character["background"] = multiple_choice(
        "Wandering Orphan", 
        "Forest Child",
        "Noble Dropout",
        "Quiet Scholar"
    )
    background = character["background"]
    time.sleep(1)

    say(dialog["backgrounds"][character["background"]]["intro"].format(name=name), 3)

    say(dialog["static"]["ask_traits"], 2)
    say("\nTraits: \n")
    say(dialog["static"]["trait_options"][0], 0)
    say(dialog["static"]["trait_options"][1], 0)
    say(dialog["static"]["trait_options"][2], 0)
    say(dialog["static"]["trait_options"][3], 0)

    character["traits"] = multiple_choice(
        ["confident", "decisive", "inspiring"],
        ["compassionate", "nurturing", "selfless"],
        ["bold", "independent", "disruptive"],
        ["analytical", "wise","strategic"]
    )
    trait_1 = character["traits"][0]
    time.sleep(1)

    say(dialog["traits"][trait_1])
    say(dialog["backgrounds"][character["background"]][trait_1])

    