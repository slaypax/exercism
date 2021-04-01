def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""

    tracking_index = 0
    for letter in text:
        print(letter)
        if letter.lower() in alphabet:
            tracking_index = alphabet.index(letter.lower()) + key
            encoded_char = alphabet[tracking_index % 26] if letter.islower() else alphabet[tracking_index % 26].upper()
            cipher += encoded_char
        else:
            cipher += letter

    return cipher