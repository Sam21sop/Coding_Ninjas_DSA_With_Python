from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)


def DFS(graph, start_vertex, visited):
    '''Function to perform Depth-first Search to find the connected component'''
    visited[start_vertex] = True
    for neighbore in graph[start_vertex]:
        if not visited[neighbore]:
            DFS(graph, neighbore, visited)


def countConnectedGroup(V, E, edges):
    '''Function Count the number of connected Graph'''
    graph = defaultdict(list)
    for edge in edges:                      #create adjancy list
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * V
    connecte_groups = 0
    for i in range(V):
        if not visited[i]:
            DFS(graph, i, visited)
            connecte_groups += 1
    return connecte_groups


def main():
    V, E = map(int, stdin.readline().strip().split())
    graph = []
    for i in range(E):
        a, b = map(int, stdin.readline().strip().split())
        graph.append((a, b))
    result = countConnectedGroup(V, E, graph)
    print(result)     


if __name__ == '__main__':
    main()