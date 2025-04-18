from core.utils import say, clear_terminal
from core.character import create_character
from core.days import day_zero

def main():
    clear_terminal()
    say("========================== The Last Drop ==========================\n", 2)

    test_character = {"rep": 0, "gold": 0, "name": "Goku", "background": "Scholar", "traits": ["bold", "independent", "disruptive"]}
    #character = create_character()
    day_zero(test_character)
    
    #say(f"\nDEBUG: {character}")

if __name__ == "__main__":
    main()