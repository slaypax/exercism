class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        split_matrix_string = matrix_string.split('\n')

        for item in split_matrix_string:
            # make rows [['1', '2'], ['3', '4']]
            row = item.split(" ")
            self.matrix.append(list(map(int, row)))

    def row(self, index):
        # matrix is a 2d array of rows
        return self.matrix[index - 1]


    def column(self, index):
        # get the item at the column index for each row in the matrix
        return [row[index - 1] for row in self.matrix]
