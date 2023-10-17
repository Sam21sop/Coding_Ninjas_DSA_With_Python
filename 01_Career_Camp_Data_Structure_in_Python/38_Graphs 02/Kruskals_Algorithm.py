class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def minimal_spanning_tree(self):
        result = []
        i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.vertices)]
        
        def find_parent(x):
            if parent[x] == x:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union(x, y):
            x_root = find_parent(x)
            y_root = find_parent(y)
            parent[x_root] = y_root

        while len(result) < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            u_root = find_parent(u)
            v_root = find_parent(v)
            if u_root != v_root:
                result.append([u, v, w])
                union(u_root, v_root)
        
        for u, v, w in result:
            if u < v:
                print("{} {} {}".format(u, v, w))
            else:
                print("{} {} {}".format(v, u, w))

def main():
    V, E = map(int, input().strip().split())
    g = Graph(V)
    for _ in range(E):
        ui, vi, wi = map(int, input().split())
        g.add_edge(ui, vi, wi)

    g.minimal_spanning_tree()

if __name__ == '__main__':
    main()