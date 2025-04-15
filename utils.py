import time
import os
import platform

def say(text, delay=1):
    print(text)
    time.sleep(delay)

def clear_terminal():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def multiple_choice(a, b, c, d):
    while True:
        choice = input("\n> ").strip().upper()
        if choice == "A":
            return a
        elif choice == "B":
            return b
        elif choice == "C":
            return c
        elif choice == "D":
            return d
        else:
            say("A curious choice... but not valid. Pick A, B, C, or D.", 0)