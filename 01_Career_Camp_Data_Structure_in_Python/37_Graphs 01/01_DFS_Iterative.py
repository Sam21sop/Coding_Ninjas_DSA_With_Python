def DFS_Iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    
def main():
    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'D', 'E'],
        'C' : ['A', 'F'],
        'D' : ['B'],
        'E' : ['B', 'F'],
        'F' : ['C', 'E']
    }
    start_node = input('Enter starting node: ')
    DFS_Iterative(graph, start_node)


if __name__ == '__main__':
    main()