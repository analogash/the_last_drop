import time
from utils import say

def create_character():
    character = {}
    say("Welcome to my shop, darling...")
    say("You must be the new apprentice I was expecting!\n")
    say("Tell me, what was your name again?", 0)
    name = input("> ")
    time.sleep(1)
    
    say(f"\nOh of course, pleasure to meet you {name}!")
    say("\nForgive me, I have been a bit scatter-brained lately.", 2)
    say("Truth be told, I could really use an extra pair of hands around here.")
    say("...", 2)

    say(f"So, {name}, tell me a little about your past.")
    say("I remember you were:\n", 0)
    say("A:  A Wandering Orphan", 0)
    say("B:  A Forest Child", 0)
    say("C:  A Noble Dropout", 0)
    say("D:  Quiet Scholar", 0)
    background = input("> ")
