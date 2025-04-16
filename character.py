import time, json
from utils import say, multiple_choice

def create_character():
    with open("dialog.json", "r") as file:
        dialog = json.load(file)

    character = {"rep": 0, "gold": 0}
    say(dialog["intro"]["welcome"], 1)
    say(dialog["intro"]["apprentice_intro"], 2)
    say(dialog["intro"]["ask_name"])
    name = input("\n" + "-" * 55 + "\n> ")
    character["name"] = name
    say("-" * 55 + "\n")
    time.sleep(1)
    
    say(dialog["intro"]["hello_name"].format(name=name), 2)
    say(dialog["intro"]["scatter_brain"], 1)
    say("..." + "\033[F", 2)
    say(dialog["intro"]["need_help"], 2)    
    say(dialog["intro"]["ask_background"].format(name=name), 2)
    say(dialog["intro"]["background_options"][0])
    say(dialog["intro"]["background_options"][1])
    say(dialog["intro"]["background_options"][2])
    say(dialog["intro"]["background_options"][3])

    character["background"] = multiple_choice(
        "Wandering Orphan", 
        "Forest Child",
        "Noble Dropout",
        "Quiet Scholar"
    )
    background = character["background"]
    time.sleep(1)

    say(dialog["backgrounds"][character["background"]].format(name=name), 3)

    say(dialog["intro"]["ask_traits"], 2)
    say("\nTraits:", 1)
    say(dialog["intro"]["trait_options"][0])
    say(dialog["intro"]["trait_options"][1])
    say(dialog["intro"]["trait_options"][2])
    say(dialog["intro"]["trait_options"][3])

    character["traits"] = multiple_choice(
        ["confident", "decisive", "inspiring"],
        ["compassionate", "nurturing", "selfless"],
        ["bold", "independent", "disruptive"],
        ["analytical", "wise","strategic"]
    )
    trait_1 = character["traits"][0]
    time.sleep(1)

    say(dialog["intro"]["trait_response"], 1)
    say(dialog["traits"][character["background"]][trait_1].format(name=name))

    return character