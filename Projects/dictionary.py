import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(word, data.keys())) > 0:
        print('did you mean %s instead?' %get_close_matches(word,data.keys())[0])
        decide = input('press y for yes or n for no: ')
        if decide == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return 'Invalid word'
    else:
        return 'You have an unknown word'

word = input("Enter the word you want to search: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)