def is_isogram(string):
    characters = {}
    valid_repeats = ["-", " "]

    for c in string:
        normalized_c = c.lower()
        if normalized_c not in characters:
            characters[normalized_c] = 0
        else:
            characters[normalized_c] += 1
            
    for character, count in characters.items():
        if character not in valid_repeats:
            if count > 0:
                return False
    return True
