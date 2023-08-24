class Matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data


    @classmethod
    def from_input(cls):
        operation = input()
        rows1, cols1 = map(int, input().split())
        data1 = [list(map(int, input().split())) for _ in range(rows1)]
        matrix1 = cls(rows1, cols1, data1)
        if operation == 'add':
            rows2, cols2 = map(int, input().split())
            data2 = [list(map(int, input().split())) for _ in range(rows2)]
            matrix2 = cls(rows2, cols2, data2)
            return operation, matrix1, matrix2
        elif operation in ['multiply', 'transpose', 'rotate']:
            return operation, matrix1
        else:
            raise ValueError("Invalid operation")


    def display(self):
        for row in self.data:
            print(*row)


    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result_data = []
        for i in range(self.rows):
            result_data.append([self.data[i][j] + other.data[i][j] for j in range(self.cols)])
        return Matrix(self.rows, self.cols, result_data)


    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result_data = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                element = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(element)
            result_data.append(row)
        return Matrix(self.rows, other.cols, result_data)


    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(self.cols, self.rows, transposed_data)


    def rotate_by_90(self):
        rotated_data = [[self.data[self.rows - 1 - j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(self.cols, self.rows, rotated_data)


def main():
    operation, matrix1, *args = Matrix.from_input()
    if operation == 'add':
        matrix2 = args[0]
        result = matrix1.add(matrix2)
    elif operation == 'multiply':
        matrix2 = args[0]
        result = matrix1.multiply(matrix2)
    elif operation == 'transpose':
        result = matrix1.transpose()
    elif operation == 'rotate':
        result = matrix1.rotate_by_90()
    result.display()


if __name__ == '__main__':
    main()