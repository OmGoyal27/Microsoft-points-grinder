from pathlib import Path
import json
import pyautogui as pg
import random
import time
import keyboard

def on_right_ctrl(event):                       # Checks to perform the main event
    if event.name == 'right ctrl':
        main()

def extract():                                  # Extracts the words
    path = Path("words.json")
    content = json.loads(path.read_text(encoding='utf-8'))
    return content

def startt():                                   # Extracts the starting words
    path = Path("start.json")
    content = json.loads(path.read_text(encoding='utf-8'))
    return content

words = extract()
starting_words = startt()

def write(words, starting_words, length):       # Does everything, like type something and hit enter
    for x in range(length):
        random_start = random.choice(starting_words)
        pg.typewrite(random_start)
        pg.typewrite(" ")
        random_word = random.choice(words)
        pg.typewrite(random_word)
        pg.typewrite(" ")
    pg.hotkey("return")

def new_tab():                                   # Opens a new tab
    pg.hotkey("ctrl", "t")
    time.sleep(1)

def main():                                     # Selects a random length and perform the grinding
    global words
    length = random.randint(1, 10)
    new_tab()
    write(words, length)


keyboard.on_press(on_right_ctrl)                 # Hooks the keyboard event

input("Press enter to exit...")                  # Keeps the program running