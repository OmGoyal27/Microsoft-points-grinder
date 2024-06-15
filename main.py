from pathlib import Path
import json
import pyautogui as pg
import random
import time

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
    random_start = random.choice(starting_words)
    pg.typewrite(random_start)
    pg.typewrite(" ")

    for x in range(length):
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
    write(words, starting_words, length)

time.sleep(3)

for i in range(100):
    try:
        main()
        time.sleep(5)
    except KeyboardInterrupt:
        print("Bye...")
        break