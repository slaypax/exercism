alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"
numbers = "1234567890"


def encode(plain_text):
    encoded = ""
    plain_text = plain_text.replace(" ", "")
    for c in plain_text:
        if c.lower() in alphabet:
            encoded += cipher[alphabet.index(c.lower())]
        elif c in numbers:
            encoded += c
    encoded = ' '.join([encoded[i:i+5] for i in range(0, len(encoded), 5)])

    return encoded

def decode(ciphered_text):
    decoded = ""
    ciphered_text = ciphered_text.replace(" ", "")
    for c in ciphered_text:
        if c in alphabet:
            decoded += alphabet[cipher.index(c)]
        elif c in numbers:
            decoded += c
    return decoded