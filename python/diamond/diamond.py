# def rows(letter):
#     letters = ''.join([chr(c) for c in range(ord('A'), ord('Z'))])
#     n = letters.index(letter)
#     rows = list(range(n)) + list(range(n)[::-1])
    
#     def get_row(i):
#         chars = [' '] * len(rows)
#         chars[n + i] = chars[n - i] = letters[i]
#         return ''.join(chars)
#     print(list(map(get_row, rows)))
#     return list(map(get_row, rows))

def rows(letter):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = letters.index(letter)
    rows = list(range(n)) + list(range(n, -1, -1))
    print(rows)

    def get_row(i):
        chars = [' '] * len(rows)
        chars[n + i] = chars[n - i] = letters[i]
        return ''.join(chars)
    print(list(map(get_row, rows)))
    return list(map(get_row, rows))

rows("B")
rows("C")