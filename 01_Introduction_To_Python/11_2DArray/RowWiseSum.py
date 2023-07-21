from sys import stdin
# import numpy as np

def row_wise_sum(matrix, n_rows, m_cols):
    for i in range(n_rows):
        row_sum = 0
        for j in range(m_cols):
            row_sum = row_sum + matrix[i][j]
        print(row_sum, end=' ')
    

def take2d_input():
    li = stdin.readline().strip().split()
    n_rows = int(li[0])
    m_cols = int(li[1])
    matrix = [list(map(int, stdin.readline().strip().split())) for row in range(n_rows)]
    return matrix, n_rows, m_cols

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        matrix, n_rows, n_cols = take2d_input()
        row_wise_sum(matrix, n_rows, n_cols)
        print()
        t -= 1

'''
1
4 2 
1 2 
3 4 
5 6 
7 8
'''