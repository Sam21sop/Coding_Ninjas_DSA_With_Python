from sys import stdin

def get_min_straingth(grid):
    rows = len(grid)
    cols = len(grid[0])
    subproblem_memo = [[0] * cols for _ in range(rows)]

    subproblem_memo[rows-1][cols-1] = max(1, 1-grid[rows-1][cols-1])
    for i in range(rows-2, -1, -1):
        subproblem_memo[i][cols-1] = max(subproblem_memo[i+1][cols-1] - grid[i][cols-1], 1)
    
    for j in range(cols-2, -1, -1):
        subproblem_memo[rows-1][j] = max(subproblem_memo[rows-1][j+1] - grid[rows-1][j], 1) 
    
    for i in range(rows-2, -1, -1):
        for j in range(cols-2, -1, -1):
            subproblem_memo[i][j] = max((min(subproblem_memo[i+1][j], subproblem_memo[i][j+1]) - grid[i][j]), 1)
    
    return subproblem_memo[0][0]


def take_input():
    n, m = [int(i) for i in input().strip().split()]
    mat = [[]] * n
    if m == 0:
        return mat
    return [[int(i) for i in input().strip().split()] for _ in range(n)]

def main():
    t = int(input())
    for _ in range(t):
        mat = take_input()
        print(get_min_straingth(mat))


if __name__ == '__main__':
    main()

# 3
# 2 3
# 0 1 -3
# 1 -2 0
# 2 2
# 0 1
# 2 0
# 3 4
# 0 -2 -3 1
# -1 4 0 -2
# 1 -2 -3 0