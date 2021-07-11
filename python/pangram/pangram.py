# Determine if a sentence is a pangram.
# Work with sets since pangrams aren't concerned with alphabetical order.

import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence = set(sentence.lower())
    return sentence >= alphabet
