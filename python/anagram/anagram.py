def find_anagrams(word, candidates):
    anagrams = []
    sorted_word = sorted(word.lower())
    for candidate in candidates:
        if sorted(candidate.lower()) == sorted_word and candidate.lower() != word.lower():
            anagrams.append(candidate)
    return anagrams