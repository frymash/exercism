import re

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = []
        self.columns = []

        # split the matrix str into rows (in str). py3 interprets str literals as unicode strs --> search criteria must be a raw string
        strRows = re.findall(r'[\r\n]?\d.+', self.matrix_string)

        for strRow in strRows:
            rowList = strRow.split() # row elements are split up e.g. ['\n4 5 6'] --> ['4','5','6']
            rowInt = [int(i) for i in rowList] # matrix row as list of integers e.g. ['4','5','6'] --> [4, 5, 6]
            self.rows.append(rowInt) # add rowInt list into row list

    def row(self, index:int):
        return self.rows[index-1] # return row number. indexes start from 0 but rows start from 1, thus index 0 = row 1

    def column(self, index:int):
        for i in range(len(self.rows)):
            sub_ls = []
            for row in self.rows:
                sub_ls.append(row[i])
            self.columns.append(sub_ls)
        # print(self.columns)
        return self.columns[index-1]

    def test(self):
        print(self.rows)
        self.column(1)
       

'''
# testing

matrix = Matrix("1 2 3\n4 5 6\n7 8 9")

matrix.test()
'''

