def value(colors):
    resistor_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    color_values = []

    for color in colors:
        color_values.append(str(resistor_codes.get(color)))

    return int(''.join(color_values[:2]))