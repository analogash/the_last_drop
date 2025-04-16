import time
from utils import say, clear_terminal
from character import create_character

def main():
    clear_terminal()
    say("==================== The Last Drop ====================\n")
    character = create_character()
    say(f"\nDEBUG: {character}")

if __name__ == "__main__":
    main()