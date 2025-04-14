import time
import os
import platform
from character import create_character

def clear_terminal():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def main():
    clear_terminal()
    print("======== The Last Drop ========\n")
    time.sleep(1)
    create_character()

if __name__ == "__main__":
    main()