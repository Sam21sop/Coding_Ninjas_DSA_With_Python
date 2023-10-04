from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    
def next_larger_element(root, element):
    if root is None:
        return None
    
    next_larger_node = None
    if root.data > element:
        next_larger_node = root
    
    for child in root.children:
        next_larger_in_child = next_larger_element(child, element)
        if next_larger_in_child != None:
            if next_larger_node == None or next_larger_node.data > next_larger_in_child.data:
                next_larger_node = next_larger_in_child
    
    return next_larger_node


def take_input_levelwise():
    level_order = list(map(int, stdin.readline().strip().split()))
    index = 0

    data = level_order[index]
    index += 1
    if data == -1:
        return
    
    root = TreeNode(data)
    q = Queue()
    q.put(root)
    
    while not q.empty():
        current_node = q.get()
        num_of_children = level_order[index]
        index += 1
        child_data = level_order[index : index + num_of_children]
        for child in child_data:
            node = TreeNode(child)
            current_node.children.append(node)
            q.put(node)
        index += num_of_children
    return root


def main():
    n = int(stdin.readline().strip())
    root = take_input_levelwise()
    next_larger = next_larger_element(root, n)
    if next_larger:
        print(next_larger.data)
    else:
        print(float('-inf'))



if __name__ == '__main__':
    main()


# Input:
# 21
# 10 3 20 30 40 2 40 50 0 0 0 0 

# Output:
# 30
