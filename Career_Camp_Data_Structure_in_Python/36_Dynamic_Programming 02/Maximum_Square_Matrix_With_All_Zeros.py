from sys import stdin

def find_max_sqr_mat(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix)
    max_side = 0

    subproblem_memo = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if matrix[i-1][j-1] == 0:
                subproblem_memo[i][j] = min(subproblem_memo[i-1][j], subproblem_memo[i][j-1], subproblem_memo[i-1][j-1]) + 1
                max_side = max(max_side, subproblem_memo[i][j])
    return max_side


def take_input():
    m, n = [int(i) for i in input().strip().split()]
    mat = [[]] * m
    if m == 0:
        return m, n, mat
    for i in range(m):
        mat[i] = [int(i) for i in input().strip().split()]
    return m, n, mat


def main():
    m, n, mat = take_input()
    res = find_max_sqr_mat(mat)
    print(res)

if __name__ == '__main__':
    main()