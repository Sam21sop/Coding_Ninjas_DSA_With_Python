'''
Time complexity: O(n*m)
Space Complexity: O(n*m)
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(board, x, y, from_x, from_y, color, n, m, visited):
    ans = False
    if x < 0 or x >= n or y < 0 or y >= m:
        return ans
    if board[x][y] != color:
        return ans
    if visited[x][y]:
        return True
    visited[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x == from_x and new_y == from_y:
            continue
        ans |= DFS(board, new_x, new_y, x, y, color, n, m, visited)
    return ans


def solve(board, n, m):
    visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
    ans = False
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                ans |= DFS(board, i, j, -1, -1, board[i][j], n, m, visited)
    return ans


def take_input():
    n, m = map(int, stdin.readline().strip().split())
    arr = [stdin.readline().strip() for i in range(n)]
    return arr, n, m


def main():
    arr, n, m = take_input()
    ans = solve(arr, n, m)
    if ans:
        print('true')
    else:
        print('false')

if __name__ == '__main__':
    main()