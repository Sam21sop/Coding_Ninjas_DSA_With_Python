def findMinVertex(weight, visited):
    n = len(weight)
    v = 0
    min_edge = float('inf')
    for i in range(n):
        if not visited[i] and min_edge > weight[i]:
            v = i
            min_edge = weight[i]
    return v

def main():
    n, e = map(int, input().split())
    
    graph = [[0] * n for _ in range(n)]
    weight = [float('inf')] * n
    visited = [False] * n
    parent = [0] * n
    
    weight[0] = 0
    source = 0

    for _ in range(e):
        t1, t2, cost = map(int, input().split())
        graph[t1][t2] = cost
        graph[t2][t1] = cost

    for i in range(1, n):
        source = findMinVertex(weight, visited)
        visited[source] = True
        
        for j in range(n):
            if graph[source][j] > 0 and not visited[j] and weight[j] > graph[source][j]:
                weight[j] = graph[source][j]
                parent[j] = source

    for i in range(1, n):
        if i < parent[i]:
            print(i, parent[i], weight[i])
        else:
            print(parent[i], i, weight[i])

if __name__ == "__main__":
    main()
