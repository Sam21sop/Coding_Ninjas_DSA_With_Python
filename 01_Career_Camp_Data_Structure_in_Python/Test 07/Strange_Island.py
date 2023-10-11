def strangeIsland():
    r, s = map(int, input().split())
    map_lst = []
    new_map = [["" for _ in range(12)] for _ in  range(12)]
    u = [0, 0, 1, -1]
    v = [1, -1, 0, 0]
    min_i, max_i, min_j, max_j = 100, 0, 100, 0

    for _ in range(r):
        row = input()
        map_lst.append(row)

    for i in range(r):
        for j in range(s):
            more = 0
            for k in range(4):
                x = i + u[k]
                y = j + v[k]
                if x < 0 or y < 0 or x >= r or y >= s or map_lst[x][y] == '.':
                    more += 1
            if more >= 3:
                new_map[i][j] = '.'
            else:
                new_map[i][j] = map_lst[i][j]
            
            if new_map[i][j] == 'X':
                min_i = min(min_i, i)
                min_j = min(min_j, j)
                max_i = max(max_i, i)
                max_j = max(max_j, j)
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j+1):
            print(new_map[i][j], end='')
        print()


strangeIsland()
