class Matrix:
    def __init__(self, matrix_string:str):
        self.matrix_string = matrix_string
        # next step converts matrix into a nested list of matrix rows (as integers)
        # e.g. self.matrix_string = '1 2 3\n4 5 6\n7 8 9' 
        # --> self.matrix_string.splitlines() = ['1 2 3', '4 5 6', '7 8 9']
        # --> self.rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.rows = [[int(i) for i in row.split()] for row in self.matrix_string.splitlines()]
        self.columns = []

    def row(self, rowNum:int):
        return self.rows[rowNum-1]

    def column(self, colNum:int):
        for row in self.rows:
            self.columns.append(row[colNum-1])
        return self.columns