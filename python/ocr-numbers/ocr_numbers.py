def convert(input_grid):

    ocr_map = { ' _ | ||_|': '0',
                '     |  |': '1',
                ' _  _||_ ': '2',
                ' _  _| _|': '3',
                '   |_|  |': '4',
                ' _ |_  _|': '5',
                ' _ |_ |_|': '6',
                ' _   |  |': '7',
                ' _ |_||_|': '8',
                ' _ |_| _|': '9'
                }
    
    def check_input_grid(grid):
        if len(grid) < 4:
            raise ValueError("not a valid grid")
        for i in grid:
            if len(i) != len(grid[0]) or len(i) % 3:
                raise ValueError("not a valid grid")

    check_input_grid(input_grid)
    numbers = []

    for four_lines in range(0, len(input_grid), 4):
        for i in range(0, len(input_grid[four_lines]), 3):
            ocr_str = ''.join([input_grid[four_lines][i], input_grid[four_lines][i+1], input_grid[four_lines][i+2],
                    input_grid[four_lines+1][i], input_grid[four_lines+1][i + 1], input_grid[four_lines+1][i + 2],
                    input_grid[four_lines+2][i], input_grid[four_lines+2][i + 1], input_grid[four_lines+2][i + 2]])
            if ocr_str in ocr_map:
                numbers.append(ocr_map[ocr_str])
            else:
                numbers.append('?')
        numbers.append(',')
    return ''.join(numbers)[:-1]


