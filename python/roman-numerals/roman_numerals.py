# https://learncodingfast.com/python-programming-challenge-8-integer-to-roman/
def roman(num):
    # use descending order becuase this is how the numeral is writen eg. 59 = LIX Where 50 = L and IX = 9
    nums_to_roman = {
        1000:'M', 
        900:'CM',
        500:'D', 
        400:'CD', 
        100:'C',
        90:'XC', 
        50:'L', 
        40:'XL', 
        10:'X', 
        9:'IX', 
        5:'V', 
        4:'IV', 
        1:'I'}
    romans = ""

    while num != 0:
        for arabic, roman in nums_to_roman.items():
            if num >= arabic:
                # int(2513/1000) = 2 so we know there are two 1000s 
                dividend = int(num/arabic)
                # 2513%1000 gives us 513, so make num smaller
                num %= arabic
                # add as many of given character to the roman representation as we need given the dividend
                romans += dividend * roman
    return romans