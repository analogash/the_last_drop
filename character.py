import time
from utils import say
from utils import multiple_choice

def create_character():
    character = {"rep": 0}
    say("Welcome to my shop, darling...")
    say("You must be the new apprentice I was expecting!\n")
    say("Tell me, what was your name again?", 0)
    name = input("> ")
    character["name"] = name
    time.sleep(1)
    
    say(f"\nOh of course, pleasure to meet you {name}!")
    say("\nForgive me, I have been a bit scatter-brained lately.", 2)
    say("Truth be told, I could really use an extra pair of hands around here.")
    say("...\n", 2)
    say(f"So, {name}, tell me a little about your past.")
    say("I heard you were:\n", 0)

    character["background"] = multiple_choice(
        "A Wandering Orphan", 
        "A Forest Child",
        "A Noble Dropout",
        "Quiet Scholar"
    )
    time.sleep(1)

    background_reply = {
        "A Wandering Orphan": f"That must’ve been a tough journey, {name}. I bet you developed a sharp sense of intuition along the way.",
        "A Forest Child": "How wonderful! Nature can teach us more than any book. You will love it here.",
        "A Noble Dropout": "A noble background, and yet here you are to help me. How intriguing!",
        "Quiet Scholar": "A scholar, hmm? I’m sure you’ll find the study of potions fascinating."
    }
    say(background_reply[character["background"]], 2)
    



    print(f"DEBUG:  {character}")
    