import time, json
from core.utils import *

def create_character():
    with open("data/dialog.json", "r") as file:
        dialog = json.load(file)
    character = {"rep": 0, "gold": 0}

    read_lines(dialog["intro"]["hello_world"])

    name = input("\n" + "-" * 67 + "\n> ")
    character["name"] = name
    say("-" * 67 + "\n")
    time.sleep(1)

    read_lines(dialog["intro"]["ask_background"], character)

    character["background"] = multiple_choice(
        A="Orphan",
        B="Forest",
        C="Noble",
        D="Scholar"
    )

    time.sleep(1)

    say(dialog["intro"]["backgrounds"][character["background"]].format(name=character["name"]), 3)

    read_lines(dialog["intro"]["ask_traits"])
    # say(dialog["intro"]["ask_traits"], 2)
    # say(dialog["intro"]["trait_options"][0])
    # say(dialog["intro"]["trait_options"][1])
    # say(dialog["intro"]["trait_options"][2])
    # say(dialog["intro"]["trait_options"][3])

    character["traits"] = multiple_choice(
        A=["confident", "decisive", "inspiring"],
        B=["compassionate", "nurturing", "selfless"],
        C=["bold", "independent", "disruptive"],
        D=["analytical", "wise","strategic"]
    )
    time.sleep(1)

    read_lines(dialog["trait_response"])
    say(dialog["traits"][character["background"]][character["traits"][0]].format(name=name), 4)

    return character