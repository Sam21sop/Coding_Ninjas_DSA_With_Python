from sys import stdin
MAX_VALUE = 2147483647

def min_cost_path(cost_mat, row_index=0, col_index=0):
    row_size = len(cost_mat)        #rows
    col_size = len(cost_mat[0])     #cols
    
    if row_index == row_size-1 and col_index == col_size-1:
        return cost_mat[row_index][col_index]
    
    if row_index >= row_size or col_index >= col_size:
        return MAX_VALUE
    
    ans1 = min_cost_path(cost_mat, row_index+1, col_index)
    ans2 = min_cost_path(cost_mat, row_index, col_index+1)
    ans3 = min_cost_path(cost_mat, row_index+1, col_index+1)

    result = cost_mat[row_index][col_index] + min(ans1, min(ans2, ans3))
    return result


def take_input():
    mRow, nCol = tuple(map(int, input().strip().split()))
    if mRow == 0:
        return []
    return [list(map(int, input().strip().split())) for _ in range(mRow)]


def main():
    mat = take_input()
    res = min_cost_path(mat)
    print(res)


if __name__ == '__main__':
    main()