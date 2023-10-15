from sys import setrecursionlimit
setrecursionlimit(10**6)


def __getPathDFSHelper(adjMatrix, nVertices, start_edge, end_edge, visited):
    if start_edge == end_edge:
        return list([start_edge])
    visited[start_edge] = True
    for i in range(nVertices):
        if adjMatrix[start_edge][i] == 1 and not visited[i]:
            lst = __getPathDFSHelper(adjMatrix, nVertices, i, end_edge, visited)
            if lst != None:
                lst.append(start_edge)
                return lst
    return 


def getPathDFS(adjMatrix, nVertices, start_edge, end_edge):
    visited = [False for _ in range(nVertices)]
    return __getPathDFSHelper(adjMatrix, nVertices, start_edge, end_edge, visited)


def main():
    nVertices, E = map(int, input().split())
    adjMatrix = [[0 for _ in range(nVertices)] for _ in range(nVertices)]
    for i in range(E):
        fv, sv = map(int, input().split())
        adjMatrix[fv][sv] = 1
        adjMatrix[sv][fv] = 1
    start_vertex, end_vertex = map(int, input().split())
    res = getPathDFS(adjMatrix, nVertices, start_vertex, end_vertex)
    if res != None:
        for elem in res:
            print(elem, end=' ')


if __name__ == '__main__':
    main()


