from sys import stdin

def wavePrint(matrix, n_rows, m_cols):
    for i in range(m_cols):
        if i % 2 == 0:
            for j in range(n_rows):
                print(matrix[j][i], end=' ')
        else:
            for k in range(n_rows-1, -1, -1):
                print(matrix[k][i], end=' ')
    

def take2d_input():
    li = stdin.readline().strip().split()
    n_rows = int(li[0])
    m_cols = int(li[1])
    if n_rows == 0:
        return list(), 0, 0
    matrix = [list(map(int, stdin.readline().strip().split())) for row in range(n_rows)]
    return matrix, n_rows, m_cols


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        mat, n_rows, m_cols = take2d_input()
        wavePrint(mat, n_rows, m_cols)
        t -= 1
    