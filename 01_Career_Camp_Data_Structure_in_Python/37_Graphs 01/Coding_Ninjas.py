from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

directions = [[-1, -1], [-1, 0],    [-1, 1],    [0, -1],    [0, 1],    [1, -1],    [1, 0],    [1, 1]]
pattern = ['C', 'O', 'D', 'I', 'N', 'G', 'N', 'I', 'N', 'J', 'A']


def valid(x, y, n, m):
    return x >= 0 and x < n and y >= 0 and y < m


def DFS(arr, used, x, y, index, n, m):
    if index == 11:
        return 1
    used[x][y] = True
    found = 0
    for i in range(8):
        new_x = x + directions[i][0]
        new_y = y + directions[i][1]
        if valid(new_x, new_y, n, m) and arr[new_x][new_y] == pattern[index] and used[new_x][new_y] == False:
            found = found | DFS(arr, used, new_x, new_y, index+1, n, m)
    used[x][y] = False
    return found


def solve(arr, n, m):
    found = 0
    used = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'C':
                found = DFS(arr, used, i, j, 1, n, m)
                if found != 0:
                    break
        if found != 0:
            break
    return found


def take_input():
    n, m = list(map(int, stdin.readline().strip().split()))
    arr = [stdin.readline().strip() for i in range(n)]
    return arr, n, m


def main():
    arr, n, m = take_input()
    print(solve(arr, n, m))


if __name__ == "__main__":
    main()