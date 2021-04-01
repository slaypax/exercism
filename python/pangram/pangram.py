import re

def is_pangram(sentence):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    sentence = sentence.lower()
    for c in alphabet:
        if c not in sentence:
            return False
    return True