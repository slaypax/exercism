import re

def abbreviate(words):
    # [A-Z]{2,}(?![a-z]) matches caps
    # [A-Z][a-z]+(?=[A-Z]) matches caps first, then (?=[A-Z])
    # looks ahead to stop match before next caps
    # [\'\w]+ allows apostrophes
    split_words = re.findall(r'[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w]+', words)

    # use to reject any chaeracter that isn't a-z A-Z or 0-9 
    allowed = re.compile("[^A-Za-z0-9\']")
    acronym = []
    for word in split_words:
        if word != "-":
            clean_word = allowed.sub('', word)
            acronym.append(clean_word[0].upper())
    return ''.join(acronym)
