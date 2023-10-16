from sys import stdin
def getCycles(graph, n):
    cycle_count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if graph[i][j] and graph[j][k] and graph[k][i]:
                    cycle_count += 1
    return cycle_count


def main():
    n, m = map(int, stdin.readline().strip().split())
    graph = [[None for _ in range(n)] for _ in range(n)]
    for i in range(m):
        u, v = map(int, stdin.readline().strip().split())
        graph[u][v] = True
        graph[v][u] = True
    print(getCycles(graph, n))


if __name__ == "__main__":
    main()