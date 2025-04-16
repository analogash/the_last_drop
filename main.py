from utils import say, clear_terminal
from character import create_character
from days import day_zero

def main():
    clear_terminal()
    say("==================== The Last Drop ====================\n", 2)
    character = create_character()
    day_zero(character)
    
    #say(f"\nDEBUG: {character}")

if __name__ == "__main__":
    main()