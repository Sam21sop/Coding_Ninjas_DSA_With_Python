from sys import stdin, setrecursionlimit


def isValid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def DFS(x, y, n, cake):
    if not isValid(x, y, n) or cake[x][y] == 0:
        return 0
    cake[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    size = 1
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        size += DFS(new_x, new_y, n, cake)
    return size


def find_biggest_piece(n, cake):
    max_piece_size = 0
    for i in range(n):
        for j in range(n):
            if cake[i][j] == 1:
                piece_size = DFS(i, j, n, cake)
                max_piece_size = max(max_piece_size, piece_size)
    return max_piece_size


def main():
    n = int(input())
    cake = [[int(i) for i in input().split()] for _ in range(n)]
    res = find_biggest_piece(n, cake)
    print(res)


if __name__ == '__main__':
    main()