class Processor:
    selection = None

    def main(self):
        choices = {'1.': 'Add Matrices',
                   '2.': 'Multiply matrix by a constant',
                   '3.': 'Multiply matrices',
                   '4.': 'Transpose matrix',
                   '0.': 'Exit'}
        while True:
            for k, v in choices.items():
                print(k, v)

            Processor.selection = input('Your choice: ')
            try:
                Processor.selection = int(Processor.selection)
                if Processor.selection == 1:
                    self.addition()
                elif Processor.selection == 2:
                    self.multi_scal()
                elif Processor.selection == 3:
                    self.multi_mat()
                elif Processor.selection == 4:
                    self.trans_mat()
                elif Processor.selection == 0:
                    print('Bye')
                    exit()
                else:
                    print('Invalid selection')
                    continue
            except ValueError:
                print('Invalid selection')
                continue

    def addition(self):
        a, b = map(int, input('Enter size of first matrix: ').split())
        A = Matrix(a, b)
        print('Enter first matrix')
        A.read_mat()
        a, b = map(int, input('Enter size of second matrix: ').split())
        B = Matrix(a, b)
        print('Enter second matrix')
        B.read_mat()
        Matrix.mat_add(A, B)

    def multi_scal(self):
        a, b = map(int, input('Enter size of matrix: ').split())
        A = Matrix(a, b)
        print('Enter matrix')
        A.read_mat()
        c = float(input('Enter constant: '))
        Matrix.mat_scal(A, c)

    def multi_mat(self):
        a, b = map(int, input('Enter size of first matrix: ').split())
        A = Matrix(a, b)
        print('Enter first matrix')
        A.read_mat()
        a, b = map(int, input('Enter size of second matrix: ').split())
        B = Matrix(a, b)
        print('Enter second matrix')
        B.read_mat()
        Matrix.mat_mat(A, B)

    def trans_mat(self):
        trans_choices = {'1.': 'Main diagonal',
                         '2.': 'Side diagonal',
                         '3.': 'Vertical line',
                         '4.': 'Horizontal line',
                         '0.': 'Return'}

        for k, v in trans_choices.items():
            print(k, v)
        trans_selection = int(input('Your choice: '))
        a, b = map(int, input('Enter size of matrix: ').split())
        A = Matrix(a, b)
        print('Enter matrix')
        A.read_mat()
        if trans_selection == 1:
            Matrix.m_diag_trans(A)
        elif trans_selection == 2:
            Matrix.s_diag_trans(A)
        elif trans_selection == 3:
            Matrix.v_line_trans(A)
        elif trans_selection == 4:
            Matrix.h_line_trans(A)
        elif trans_selection == 0:
            print('Bye')
            exit()
        else:
            print('Invalid selection')
            # continue


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []

    def read_mat(self):
        for i in range(self.row):
            a = list(map(float, input().split()))
            self.matrix.append(a)

    def print_mat(self):
        print('The result is:')
        for i in range(self.row):
            print(*self.matrix[i][:])
        print()

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

    @staticmethod
    def mat_mat(mat1, mat2):
        if mat1.column != mat2.row:
            print('ERROR')
        else:
            result = Matrix(mat1.row, mat2.column)
            result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
            for i in range(mat1.row):
                for j in range(mat2.column):
                    for k in range(mat2.row):
                        result.matrix[i][j] += mat1.matrix[i][k] * mat2.matrix[k][j]
            result.print_mat()

    @staticmethod
    def m_diag_trans(mat1):
        result = Matrix(mat1.column, mat1.row)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[j][i]
        result.print_mat()

    @staticmethod
    def s_diag_trans(mat1):
        result = Matrix(mat1.column, mat1.row)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[i][j]
        result.print_mat()


# BODY
start = Processor()
start.main()
