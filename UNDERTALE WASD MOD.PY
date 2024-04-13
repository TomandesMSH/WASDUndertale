import keyboard
import subprocess
import tkinter as tk
from tkinter import filedialog
import os
import time

print("Welcome to WASDUndertale!")
input("Press ENTER to continue!")
print("Press 1 to run UNDERTALE from Steam")
print("Press 2 if you want to run Undertale from a different location (you can use this to play fangames with WASD)") 
print("Press 3 if you need help")
print(" ")
print("(Confirm your selections with the ENTER key)")
print(" ")
selection = input("Choose a number: ")
if selection == "1" :
        print("Launching the Steam version of UNDERTALE!")
        print("Press ESC anytime to CANCEL the WASD arrow function!!")
        time.sleep(4)
        subprocess.run(["cmd", "/c", "start", "steam://rungameid/391540"], shell=True)

if selection == "2" :
     print("keep this script running and open the game.")
     print("this will get improved in the next update")
     input("Press ENTER -> WASD will become arrows.")

if selection == "3" :
     print("todo: make a tutorial - lazy")

def remap_keys():
    
    key_mappings = {
        "w": "up",
        "s": "down",
        "a": "left",
        "d": "right"
    }
    
    
    for original_key, remapped_key in key_mappings.items():
        keyboard.remap_key(original_key, remapped_key)


remap_keys()


keyboard.wait("esc")


keyboard.unhook_all()
print("Everything is back to normal!")
print("WASD is now WASD and arrows are now arrows.")


print("Thank you for using WASDUndertale")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

print("See more on: ")
print("        _ _   _           _       ___                                  _           __  __ ____  _   _ ")
print("   __ _(_) |_| |__  _   _| |__   / / |_ ___  _ __ ___   __ _ _ __   __| | ___  ___|  \/  / ___|| | | |")
print("  / _` | | __| '_ \| | | | '_ \ / /| __/ _ \| '_ ` _ \ / _` | '_ \ / _` |/ _ \/ __| |\/| \___ \| |_| |")
print(" | (_| | | |_| | | | |_| | |_) / / | || (_) | | | | | | (_| | | | | (_| |  __/\__ \ |  | |___) |  _  |")
print("  \__, |_|\__|_| |_|\__,_|_.__/_/   \__\___/|_| |_| |_|\__,_|_| |_|\__,_|\___||___/_|  |_|____/|_| |_|")
print("  |___/                                                                                               ")


time.sleep(3)