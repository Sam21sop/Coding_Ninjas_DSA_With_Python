from collections import deque

def printHelper(edges, v1, v2, visited):
    q = deque()
    q.append(v1)
    n = len(edges)
    while q:
        node = q.popleft()
        visited[node] = True
        if node == v2:
            print('true')
            return
        for i in range(n):
            if edges[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    print('false')


def main():
    v, e = map(int, input().split())
    edges = [[0 for _ in range(v)] for _ in range(v)]
    for i in range(e):
        fv, sv = map(int, input().split())
        edges[fv][sv] = 1
        edges[sv][fv] = 1
    v1, v2 = map(int, input().split())
    visited = [False] * len(edges[0])
    printHelper(edges, v1, v2, visited)
    

if __name__ == "__main__":
    main()