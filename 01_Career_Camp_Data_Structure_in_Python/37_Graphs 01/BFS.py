from queue import Queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


class Graph:
    def __init__(self, num_of_vertices) -> None:
        self.num_of_vertices = num_of_vertices
        self.adj_matrix = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
    

    def addEdge(self, vertex1, vertex2):
        self.adj_matrix[vertex1][vertex2] = 1
        self.adj_matrix[vertex2][vertex1] = 1

    
    def containsEdge(self, vertex1, vertex2):
        if self.adj_matrix[vertex1][vertex2] > 0:
            return True
        else:
            return False


    def removeEdge(self, vertex1, vertex2):
        if self.containsEdge(vertex1, vertex2) is False:
            return
        self.adj_matrix[vertex1][vertex2] = 0
        self.adj_matrix[vertex2][vertex1] = 0

    
    def __dfs(self, start_vertex, visited):
        q = Queue()
        q.put(start_vertex)
        visited[start_vertex] = True
        while q.empty() is False:
            edge = q.get()
            print(edge, end=' ')
            for i in range(self.num_of_vertices):
                if self.adj_matrix[edge][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
    

    def bfs(self):
        visited = [False for _ in range( self.num_of_vertices)]
        for i in range(self.num_of_vertices):
            if visited[i] is False:
                self.__dfs(i, visited)


    def __str__(self) -> str:
        return str(self.adj_matrix)
    

def main():
    num_of_vertex, num_of_edge = map(int, stdin.readline().strip().split())
    graph = Graph(num_of_vertex)
    # print(graph)
    for i in range(num_of_edge):
        vertex1, vertex2 = map(int, stdin.readline().strip().split())
        graph.addEdge(vertex1, vertex2)
        # print(graph)
    graph.bfs()
    # print()
    graph.removeEdge(2, 3)
    # print()
    # print(graph)


if __name__ == '__main__':
    main()

#input:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3

#output:
# 0 1 3 2