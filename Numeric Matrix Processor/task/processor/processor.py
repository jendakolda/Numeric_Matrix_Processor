import numpy as np


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []

    def read_mat(self):
        for _ in range(self.row):
            a = list(map(int, input().split()))
            self.matrix.append(a)

    def mat_add(a, b):
        pass

# BODY
a, b = map(int, input().split())
A = Matrix(a, b)
A.read_mat()

a, b = map(int, input().split())
B = Matrix(a, b)
B.read_mat()

print(A.row == B.row and A.column == B.column)
print(A.matrix[0]+B.matrix[0])
