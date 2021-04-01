encode_char = lambda char, count : char if count == 1 else f"{count}{char}"

def decode(string):
    if not string:
        return ""

    decoded = ""
    # its easier if the counter is a string, becuase we can handle double digit counts,
    # e.g. '12W' 
    count_string = ""
    for char in string:
        if char.isdigit():
            count_string += char
            # reject all the rest of this iteration of the loop and move to the next
            # character, it should be a letter
            continue

        if count_string:
            decoded += int(count_string) * char
        else: 
            decoded += char
        count_string = ""
    return decoded

def encode(string):
    if not string:
        return ""

    encoded = ""
    previous_char = string[0]
    char_count = 1
    # start at the second char, since we already know what the first char is
    # and we need to begin counting
    for char in string[1:]:
        if char == previous_char:
            char_count += 1
        else:
            encoded += encode_char(previous_char, char_count)
            previous_char = char
            char_count = 1
    
    encoded += encode_char(previous_char, char_count)
    return encoded

encode("AABBBCCCC")    