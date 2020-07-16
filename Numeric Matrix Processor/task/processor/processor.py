import numpy as np


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []
        # self.matrix = [[0 for i in range(self.column)] for j in range(self.row)]

    def read_mat(self):
        for i in range(self.row):
            a = list(map(int, input().split()))
            self.matrix.append(a)

    def print_mat(self):
        for i in range(self.row):
            print(*self.matrix[i][:])

    @staticmethod
    def mat_add(mat1, mat2):
        if (mat1.row != mat2.row) or (mat1.column != mat2.column):
            print('ERROR')
        else:
            result = Matrix(mat1.row, mat1.column)
            result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
            for i in range(result.row):
                for j in range(result.column):
                    result.matrix[i][j] = mat1.matrix[i][j] + mat2.matrix[i][j]
            result.print_mat()

    @staticmethod
    def mat_scal(mat1, scal):
        result = Matrix(mat1.row, mat1.column)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[i][j] * scal
        result.print_mat()

# BODY

a, b = map(int, input().split())
A = Matrix(a, b)
A.read_mat()
c = int(input())
Matrix.mat_scal(A, c)
# a, b = map(int, input().split())
# B = Matrix(a, b)
# B.read_mat()
#
# Matrix.mat_add(A, B)

