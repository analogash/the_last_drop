import time
from utils import say
from utils import multiple_choice

def create_character():
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
    say(f"So, {name}, tell me a little about your past. I heard you were a:\n", 2)
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
    time.sleep(1)

    background_reply = {
        "Wandering Orphan": f"\nThat must’ve been a tough journey, {name}. I bet you developed a sharp sense of intuition along the way.",
        "Forest Child": "\nHow wonderful! Nature can teach us more than any book. You will love it here.",
        "Noble Dropout": "\nA noble background, and yet here you are to help me. I am honored!",
        "Quiet Scholar": "\nA scholar, hmm? I’m sure you’ll find the study of potions fascinating."
    }
    say(background_reply[character["background"]], 3)

    say("\nI am curious however, what makes you think you'll be good at this job?", 2)
    say ("\nTraits: \n")
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
    time.sleep(1)

    traits_reply = {
        "confident": "\nConfidence like that can move mountains... or stir very stubborn mixtures.",
        "compassionate": "\nA gentle soul. This shop could use more kindness like yours!",
        "bold": "\nOho! A rebel in the making—I like that spark in your eye.",
        "analytical": "\nWisdom and patience forge the finest potions!"
    }
    say(traits_reply[character["traits"][0]])

    print(f"DEBUG:  {character}")
    