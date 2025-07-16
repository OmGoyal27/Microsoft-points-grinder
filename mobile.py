from pathlib import Path
import json
import pyautogui as pg
import random
import time
import keyboard

def extract():                                              # Extracts all the available words
    path = Path("meanings.json")
    content = json.loads(path.read_text(encoding='utf-8'))
    return content

def startt():                                               # Extracts all the starting words
    path = Path("start.json")
    content = json.loads(path.read_text(encoding='utf-8'))
    return content

words = extract()
startin_words = startt()

def write(words):                                           # Performs the main function, i.e., to click and write words and press enter
    pg.hotkey("ctrl", "a")
    pg.hotkey("backspace")
    pg.typewrite("What is the meaning of ")
    random_word = random.choice(words)
    pg.typewrite(random_word)
    pg.hotkey("return")

def main():                                                 # Initialises everything to clean up the mess a bit
    global words
    global startin_words
    pg.click()
    write(words)
    time.sleep(4)

time.sleep(3)                                               # Waits for three seconds before starting the program, giving the user enough time to open to page
while True:
    if keyboard.is_pressed("esc"):
        break
    main()