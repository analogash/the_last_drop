import time
import os
import platform
from utils import say
from utils import clear_terminal
from character import create_character

def main():
    clear_terminal()
    print("======== The Last Drop ========\n")
    time.sleep(1)
    create_character()

if __name__ == "__main__":
    main()