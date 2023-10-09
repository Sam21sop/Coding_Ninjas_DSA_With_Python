def is_valid_move(maze, x, y, visited):
    n = len(maze)
    return x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1 and not visited[x][y]


def can_reach_destination(maze, x, y, visited):
    if x == len(maze)-1 and y == len(maze)-1:
        return True
    
    #Right, Left, Down, Up
    directions = [(0,1),(0,-1), (1,0), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = x+dx, y+dy
        if is_valid_move(maze, new_x, new_y, visited):
            visited[new_x][new_y] = True
            if can_reach_destination(maze, new_x, new_y, visited):
                return True
            visited[new_x][new_y] = False
    return False


def rat_can_reach_dest(maze):
    n = len(maze)
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    return can_reach_destination(maze, 0, 0, visited)


def main():
    n = int(input())
    maze = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        maze.append(row)
    if rat_can_reach_dest(maze):
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()