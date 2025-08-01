from pathlib import Path
import json
import pyautogui as pg
import random
import time
import webbrowser


SLEEP_TIME_PER_TAB = 3      # Adjust this as per your system performance.
NUMBER_OF_SEARCHES = 31       # Adjust this as per your wish.

class Data():
    def extract():                                  # Extracts the words
        path = Path("examples/words.json")
        content = json.loads(path.read_text(encoding='utf-8'))
        return content

    def startt():                                   # Extracts the starting words
        path = Path("examples/start.json")
        content = json.loads(path.read_text(encoding='utf-8'))
        return content

words = Data.extract()
starting_words = Data.startt()



class Interact():

    def new_tab():                                   # Opens a new tab
        pg.hotkey("ctrl", "t")
        time.sleep(1)
    
    def close_tab():
        pg.hotkey("ctrl", "w")
        time.sleep(1)

    def write(words, starting_words, length):       # Does everything, like type something and hit enter
        random_start = random.choice(starting_words)
        pg.typewrite(random_start)
        pg.typewrite(" ")

        for x in range(length):
            random_word = random.choice(words)
            pg.typewrite(random_word)
            pg.typewrite(" ")
        pg.hotkey("return")

def main():                                     # Selects a random length and perform the grinding
    global words
    length = random.randint(1, 10)
    Interact.new_tab()
    Interact.write(words, starting_words, length)
    time.sleep(4)
    Interact.close_tab()

time.sleep(SLEEP_TIME_PER_TAB)
webbrowser.open("https://rewards.bing.com/pointsbreakdown")
time.sleep(SLEEP_TIME_PER_TAB)

for i in range(NUMBER_OF_SEARCHES):
    try:
        main()
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Bye...")
        break