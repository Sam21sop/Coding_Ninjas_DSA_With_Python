def DFS_recursive(graph, start_node, visited=set()):
    if start_node not in visited:
        print(start_node, end=' ')
        visited.add(start_node)
        for neighbor in graph[start_node]:
            if neighbor not in visited:
                DFS_recursive(graph, neighbor, visited)


def main():
    graph = {
        'A':['B', 'C'],
        'B':['A', 'D', 'E'],
        'C':['A', 'F'],
        'D':['B'],
        'E':['B', 'F'],
        'F':['C', 'E']
    }
    start_node = input('Enter start Node, eg A: ')
    DFS_recursive(graph, start_node)

    
if __name__ == '__main__':
    main()