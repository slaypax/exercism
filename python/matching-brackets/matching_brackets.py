# def is_paired(input_string):
    
#     stack = []
#     valid_brackets = {")":"(","]":"[","}":"{"}

#     for char in input_string:
#         print("print stack: " + str(stack) + " - end")
#         if char in valid_brackets.values():
#             stack.append(char)
#         elif char in valid_brackets.keys():
#             if stack == [] or valid_brackets.get(char) != stack.pop():
#                 return False

#     return stack == []

def is_paired(input_string):
    counter = 0
    if input_string[0] == "}" or input_string[0] == ")" or input_string[0] == "]":
        counter +=1

    for char in input_string:
        if char == '(':
            counter += 1
        if char == ')':
            counter -= 1
        if char == '[':
            counter += 1
        if char == ']':
            counter -= 1
        if char == '{':
            counter +=1
        if char == '}':
            counter -= 1
    
    return counter == 0


is_paired("{}[]")