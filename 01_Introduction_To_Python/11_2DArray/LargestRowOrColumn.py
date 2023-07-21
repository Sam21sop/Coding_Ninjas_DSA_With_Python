from sys import stdin
MIN_VALUE = -2147483648


def find_largest(array, n_rows, m_cols):
    is_row = True
    largest_sum = MIN_VALUE 
    num = 0
    for i in range(n_rows):
        row_sum = 0
        for j in range(m_cols):
            row_sum += array[i][j]
        if row_sum > largest_sum:
            largest_sum = row_sum
            num = i
    for j in range(m_cols):
        col_sum = 0
        for i in range(n_rows):
            col_sum += array[i][j]
        if col_sum > largest_sum:
            largest_sum = col_sum
            num = j
    if is_row:
        print(f'row {num} {largest_sum}')
    else:
        print(f'col {num} {largest_sum}')
      


def take2dinput():
    li = stdin.readline().split()
    n_rows = int(li[0])
    m_cols = int(li[1])
    if n_rows == 0:
        return list(), 0, 0
    
    array = [list(map(int, stdin.readline().strip().split())) for row in range(n_rows)]
    return array, n_rows, m_cols


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        arr2d, n_rows, m_cols = take2dinput()
        find_largest(arr2d, n_rows, m_cols)
        t -= 1

'''
1
3 2
6 9 
8 5 
9 2 
'''