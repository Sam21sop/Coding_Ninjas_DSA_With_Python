from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def bfs(graph, start_node, visited):
    q = deque()
    q.append(start_node)
    visited[start_node] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True


def bfs_disconnected(graph, num_vertice):
    visited = [False] * num_vertice
    for vertex in range(num_vertice):
        if not visited[vertex]:
            bfs(graph, vertex, visited)


def main():
    num_of_vertex, num_of_edge = map(int, stdin.readline().strip().split())
    adj_matrix = [[False] * num_of_vertex for _ in range(num_of_vertex)]
    for _ in range(num_of_edge):
        a, b = map(int, stdin.readline().strip().split())
        adj_matrix[a][b] = True
        adj_matrix[b][a] = True
    graph = [[] for _ in range(num_of_vertex)]
    for i in range(num_of_vertex):
        for j in range(num_of_vertex):
            if adj_matrix[i][j]:
                graph[i].append(j)
    bfs_disconnected(graph, num_of_vertex)

    
if __name__ == "__main__":
    main()


#input:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3

#output:
# 0 1 3 2