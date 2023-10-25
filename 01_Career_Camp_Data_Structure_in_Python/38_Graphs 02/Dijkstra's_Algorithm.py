from sys import stdin, setrecursionlimit, maxsize

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]


    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    
    def dijkstra(self, source):
        visited = [False] * self.v
        distance = [maxsize] * self.v
        distance[source] = 0

        for _ in range(self.v):
            min_dist = maxsize
            min_vert = -1
            for v in range(self.v):
                if not visited[v] and distance[v] < min_dist:
                    min_dist = distance[v]
                    min_vert = v
            visited[min_vert] = True
            for v in range(self.v):
                if not visited[v] and self.graph[min_vert][v] != 0 and distance[min_vert] != maxsize and distance[min_vert] + self.graph[min_vert][v] < distance[v]:
                    distance[v] = distance[min_vert] + self.graph[min_vert][v]
        return distance 
    

def main():
    v, e = map(int, input().split())
    g = Graph(v)
    for _ in range(e):
        ei, vi, wi = map(int, input().split())
        g.add_edge(ei, vi, wi)
    distance = g.dijkstra(0)
    for vertex, distance in enumerate(distance):
        print('{} {}'.format(vertex, distance))


if __name__ == '__main__':
    main()

'''
sample input:
4 4
0 1 3
0 3 5
1 2 1
2 3 8

sample output:
0 0
1 3
2 4
3 5
'''