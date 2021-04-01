def score(word):
    scores = {
        1: set(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']),
        2: set(['D', 'G']),
        3: set(['B', 'C', 'M', 'P']),
        4: set(['F', 'H', 'V', 'W', 'Y']),
        5: set(['K']),
        8: set(['J', 'X']),
        10: set(['Q', 'Z'])
    }
    score = 0
    for letter in word:
        for points, letters in scores.items():
            if letter.upper() in letters:
                score += points
    return score