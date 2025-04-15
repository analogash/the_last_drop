import time, json
from utils import say, multiple_choice

def create_character():
    with open("dynamic_dialog.json", "r") as file:
        dynamic_dialog = json.load(file)

    character = {"rep": 0}
    say("Welcome to my shop, darling...")
    say("You must be the new apprentice I was expecting!\n", 2)
    say("Tell me, what was your name again?")
    name = input("\n> ")
    character["name"] = name
    time.sleep(1)
    
    say(f"\nOh of course, pleasure to meet you {name}!", 2)
    say("\nForgive me, I have been a bit scatter-brained lately.", 2)
    say("Truth be told, I could really use an extra pair of hands around here.", 2)
    say("...\n")
    say(f"So {name}, tell me a little about your past. I heard you were a:\n", 2)
    say(f"A:  Wandering Orphan", 0)
    say(f"B:  Forest Child", 0)
    say(f"C:  Noble Dropout", 0)
    say(f"D:  Quiet Scholar", 0)

    character["background"] = multiple_choice(
        "Wandering Orphan", 
        "Forest Child",
        "Noble Dropout",
        "Quiet Scholar"
    )
    background = character["background"]
    time.sleep(1)

    say(dynamic_dialog["backgrounds"][character["background"]]["intro"], 3)

    say("\nI am curious however, what makes you think you'll be good at this job?", 2)
    say("\nTraits: \n")
    say(f"A:  Confident, decisive, and inspiring.", 0)
    say(f"B:  Compassionate, nurturing, and selfless.", 0)
    say(f"C:  Bold, independent, and disruptive.", 0)
    say(f"D:  Analytical, wise, and strategic.", 0)

    character["traits"] = multiple_choice(
        ["confident", "decisive", "inspiring"],
        ["compassionate", "nurturing", "selfless"],
        ["bold", "independent", "disruptive"],
        ["analytical", "wise","strategic"]
    )
    trait_1 = character["traits"][0]
    time.sleep(1)

    say(dynamic_dialog["traits"][trait_1])
    say(dynamic_dialog["backgrounds"][character["background"]][trait_1])

    