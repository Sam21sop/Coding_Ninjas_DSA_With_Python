def is_valid_move(maze, x, y, visited):
    size = len(maze)
    return x >= 0 and x < size and y >= 0 and y < size and maze[x][y] == 1 and not visited[x][y]


def display_path(path):
    for row in path:
        print(*row, end=' ')
    print()


def find_path(maze, x, y, visited, path):
    size = len(maze)
    if x == size -1 and y == size - 1:
        path[x][y] = 1
        display_path(path)
        return
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]         # Right, left, down, up
    for dir_x, dir_y in directions:
        new_x = x + dir_x
        new_y = y + dir_y
        if is_valid_move(maze, new_x, new_y, visited):
            visited[new_x][new_y] = True
            path[new_x][new_y] = 1
            find_path(maze, new_x, new_y, visited, path)
            path[new_x][new_y] = 0
            visited[new_x][new_y] = False


def main():
    maze_size = int(input())
    maze = [list(map(int, input().split())) for _ in range(maze_size)]
    visited = [[False for _ in range(maze_size)] for _ in range(maze_size)]
    visited[0][0] = True
    path = [[0 for _ in range(maze_size)] for _ in range(maze_size)]
    path[0][0] = 1
    find_path(maze, 0, 0, visited, path)


if __name__ == '__main__':
    main()