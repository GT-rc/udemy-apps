"""
Console program to search for word definitions. Checks if word is in the included json file and makes suggestions 
for common misspellings.
"""

import json
from difflib import get_close_matches

f = "./data.json"
data = json.load(open(f, 'r'))

def in_dict(word):
    """Checks if the word is in the dict, and returns def if it is."""
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        response = input("Did you mean %s? Enter [Y] if yes, and [N] if no: " % get_close_matches(word, data.keys())[0])
        if response.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif response.lower() == 'n':
            return "That word is not in my dictionary. Please try a different word or another resource."
        else:
            return "I didn't understand that entry."
    else:
        return "That word is not in my dictionary. Please try a different word or another resource."


def main():
    """Main program"""
    user_word = input("Enter a word: ").lower()
    output = in_dict(user_word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

main()
