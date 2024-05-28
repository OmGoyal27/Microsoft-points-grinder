from pathlib import Path
import json

path = Path("words.json")

words = json.loads(path.read_text(encoding='utf-8'))

for word in words:                                      # Prints out all the words
    print(word)