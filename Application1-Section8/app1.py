# TODO 1: create a function to search the dict for a key and print out the output

import json
from difflib import SequenceMatcher, get_close_matches

f = "./data.json"
data = json.load(open(f, 'r'))

def in_dict(word):
    """Checks if the word is in the dict, and returns def if it is."""
    if word in data:
        return data[word]
    elif get_close_matches(word, data.keys()) != None:
        return "Did you mean " + get_close_matches(word, data.keys())[0] + "?"
    else:
        return "That word is not in my dictionary. Please try a different word or another resource."

word = input("Enter a word: ").lower()

print(in_dict(word))


