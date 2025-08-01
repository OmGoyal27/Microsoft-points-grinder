from pathlib import Path
import json

path = Path("examples/words.json")
words = json.loads(path.read_text(encoding='utf-8'))
while True:                                                 # Adds words in the words.json file
    new_word = input("Enter the word: ")
    if new_word != "save":
        if not new_word in words:
            words.append(new_word)
    else:
        print("Saved!")
        path.write_text(json.dumps(words))