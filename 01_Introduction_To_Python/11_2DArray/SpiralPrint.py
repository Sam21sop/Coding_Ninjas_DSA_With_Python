from sys import stdin

def spiral_print(matrix, n_rows, m_cols):
    k = 0
    l = 0
    while k < n_rows and l < m_cols:
        for i in range(l, m_cols):
            print(matrix[k][i], end=' ')
        k += 1

        for i in range(k, n_rows):
            print(matrix[i][m_cols-1], end=' ')
        m_cols -= 1

        if k < n_rows:
            for i in range(m_cols-1, l-1, -1):
                print(matrix[n_rows-1][i], end=' ')
        n_rows -= 1

        if l < m_cols:
            for i in range(n_rows-1, k-1, -1):
                print(matrix[i][l], end=' ')
        l += 1


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
        mat, n, m = take2d_input()
        spiral_print(mat, n, m)
        t -= 1


'''
1
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
'''
