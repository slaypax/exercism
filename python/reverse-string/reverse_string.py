# def reverse(text):
#     return text[::-1]

# def reverse(text):
#     reversed_string = []
#     for i in range(len(text) -1, -1, -1):
#         reversed_string += text[i]
#     return ''.join(reversed_string)

def reverse(text):
    return ''.join([i for i in reversed(text)])
