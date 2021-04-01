def saddle_points(matrix):

    # not a mtrix unless all rows are the same length as the first row
    is_matrix = lambda matrix : not any(len(row) != len(matrix[0]) for row in matrix)
    get_coords = lambda x, y : {"row": x + 1, "column": y + 1}
    
    if is_matrix(matrix):
        # find saddle point
        rows, columns = matrix, list(zip(*matrix))
        all_saddle_points = []
        for x, row in enumerate(matrix):
            for y, value in enumerate(row):
                if max(rows[x]) == min(columns[y]):
                    all_saddle_points.append(get_coords(x, y))
        print(all_saddle_points)
        return all_saddle_points
    else:
        raise ValueError("this is not a matrix.")
    pass