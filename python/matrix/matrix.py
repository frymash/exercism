from typing import List

class Matrix:
    def __init__(self, matrix_string:str):
        self.rows = [[int(i) for i in row.split()] for row in matrix_string.splitlines()]

    def row(self, rowNum:int) -> List[int]:
        return self.rows[rowNum-1]

    def column(self, colNum:int) -> List[int]:
        columns = [row[colNum-1] for row in self.rows]
        return columns