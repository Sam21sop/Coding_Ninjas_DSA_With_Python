from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(graph, start_vertex, visited):
    visited[start_vertex] = True
    for i in range(len(graph)):
        if graph[start_vertex][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)


def isConnected(graph):
    if len(graph) == 0:
        return True
    visited = [False] * len(graph)
    dfs(graph, 0, visited)
    for elem in  visited:
        if not elem:
            return False
    return True


def main():
    V, E = map(int, input().split())
    graph = [[0] * V for _ in range(V)]
    for _ in range(E):
        sv, ev = map(int, input().split())
        graph[sv][ev] = 1
        graph[ev][sv] = 1
    if isConnected(graph):
        print('true')
    else:
        print('false')


if __name__ == "__main__":
    main()