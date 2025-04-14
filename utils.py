import time
import os
import platform

def say(text, delay=1):
    print(text)
    time.sleep(delay)

def clear_terminal():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)