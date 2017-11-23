# TODO 1: create a function to search the dict for a key and print out the output

import json

f = "./data.json"
data = json.load(open(f, 'r'))

def define_word(search_key):
    """Find and print a key from the data var."""
    return data[search_key]

def in_dict(word):
    """Checks if the word is in the dict."""
    if word in data:
        return define_word(word)
    else:
        return "That word is not in my dictionary, sorry. Please try a different word or another resource."

word = input("Enter a word: ")

print(in_dict(word))