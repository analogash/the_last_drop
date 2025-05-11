import json
from core.utils import *

def day_zero(character):
    # Import dialog
    with open("data/dialog.json", "r") as file:
        dialog = json.load(file)
   
    # Read intro 
    read_lines(dialog["zero_intro"], character)

    # Prep for look/go section
    counter = 0
    look_list = dialog["intro_look"][character["background"]]

    # Look or Go
    while True:
	    # Prompt
        choice = multiple_choice(A="A:  Look Around", B="B:  Go Outside")

        # Cycle through look dialog
        if choice[0] is "A":
            narrate(look_list[counter]["text"])
            counter = (counter + 1) % len(look_list)
        
	# Move onto go section
        if choice[0] is "B":
            read_lines(dialog["intro_go"][character["background"]], character)
            break

    # Look, Collect, Go 
    while True:
        # Prompt
        choice = multiple_choice(A="A:  Look Around", B="B:  Collect Herbs", C="C:  Go Inside")
        collected = False
         
        if choice[1] is "A":
            narrate(dialog["herbs_look"][character["background"]], 3)

        if choice[0] is "B":
            collected = True
            read_lines(dialog["herbs_collect"][character["background"]], character)
            while True:
                choice = multiple_choice(A="A:  Look Around", B="B:  Go Inside")
                if choice[0] is "A":
                    narrate(dialog["herbs_look"][character["background"]], 3)
                if choice[0] is "B":
                    read_lines(dialog["herbs_go"][character["background"]][character["traits"]], character)        
                    break
        if collected:
            break

        if choice[0] is "C":
            read_lines(dialog["herbs_go_bad"], character)

