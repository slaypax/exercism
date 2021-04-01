# def count_words(sentence):
#     words = OrderedDict()
#     # [A-Z]{2,}(?![a-z]) matches caps
#     # [A-Z][a-z]+(?=[A-Z]) matches caps first. 
#     # (?=[A-Z]) part looks ahead to stop match before next cap
#     # [\'\w\-]+
#     split_sentence = re.findall(r'[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+', sentence)
#     for word in split_sentence:
#         normalized_word = word.lower()
#         if normalized_word not in words:
#             words[normalized_word] = 1
#         else:
#             words[normalized_word] += 1

#     return dict(words)
import re
import string

def count_words(sentence):
    words = sentence.replace(',', ' ')
    words = words.replace('_', ' ')
    words = words.replace(';', ' ')
    words = words.lower().split()
    allowed = re.compile("[A-Za-z0-9\']")
    clean = []
    for word in words:
        wclean = ''.join(l for l in word if allowed.match(l))
        wclean = wclean.strip("'")
        clean.append(wclean)
    return dict((word, clean.count(word)) for word in set(clean))