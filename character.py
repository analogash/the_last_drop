import time, json
from utils import say, narrate, multiple_choice

def create_character():
    with open("dialog.json", "r") as file:
        dialog = json.load(file)

    character = {"rep": 0, "gold": 0}
    say(dialog["intro"]["welcome"], 1)
    say(dialog["intro"]["apprentice_intro"], 2)
    narrate(dialog["intro"]["look_around"],3)
    say(dialog["intro"]["ask_name"])
    name = input("\n" + "-" * 55 + "\n> ")
    character["name"] = name
    say("-" * 55 + "\n")
    time.sleep(1)
    
    say(dialog["intro"]["hello_name"].format(name=name), 2)
    narrate(dialog["intro"]["bow"], 2)
    say(dialog["intro"]["scatter_brain"], 1)
    say("..." + "\033[F", 2)
    say(dialog["intro"]["need_help"], 3)
    say(dialog["intro"]["glad"], 3)
    say(dialog["intro"]["ask_background"].format(name=name), 2)
    say(dialog["intro"]["background_options"][0])
    say(dialog["intro"]["background_options"][1])
    say(dialog["intro"]["background_options"][2])
    say(dialog["intro"]["background_options"][3])

    character["background"] = multiple_choice(
        A="Wandering Orphan",
        B="Forest Child",
        C="Noble Dropout",
        D="Quiet Scholar"
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
        A=["confident", "decisive", "inspiring"],
        B=["compassionate", "nurturing", "selfless"],
        C=["bold", "independent", "disruptive"],
        D=["analytical", "wise","strategic"]
    )
    time.sleep(1)

    say(dialog["intro"]["trait_response"], 1)
    say(dialog["traits"][character["background"]][character["traits"][0]].format(name=name), 4)

    return character