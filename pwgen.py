#!/usr/bin/env python3

import random
from random_word import RandomWords

r = RandomWords()

with open('/usr/share/dict/american-english') as f:
    words = [line.rstrip() for line in f]


def wordGenerator(**kwargs):
    if False:  # random_word requires apikey
        while True:
            try:
                word = r.get_random_word(**kwargs)
            except Exception as e:
                continue
            if word.isalnum():
                yield word
    else:
        while True:
            word = words[random.randint(0, len(words))]
            if len(word) < 5:
                continue
            if len(word) > 15:
                continue
            if word.isalnum():
                yield word


adjgen = wordGenerator(includePartOfSpeech='adjective',
                       minLength=5, maxLength=12)
noungen = wordGenerator(includePartOfSpeech='noun', minLength=5, maxLength=12)

outpwd = next(adjgen).capitalize() + \
    next(adjgen).capitalize() + next(noungen).capitalize()

outpwd += "!" + str(random.randint(111, 999))
print(outpwd)
