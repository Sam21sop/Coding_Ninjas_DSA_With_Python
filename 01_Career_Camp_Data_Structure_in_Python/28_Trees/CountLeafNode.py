from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def leaf_node(root:TreeNode):
    if root is None:
        return 0

    if len(root.children) == 0:
        return 1
    
    leaf_node_count = 0
    for child_node in root.children:
        leaf_node_count += leaf_node(child_node)

    return leaf_node_count


def take_input_levelwise():
    level_order = list(map(int, stdin.readline().strip().split()))
    index = 0
    data = level_order[index]
    index += 1
    if data == -1:
        return None
    root = TreeNode(data)
    q = Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        num_of_children = level_order[index]
        index += 1
        child_data = level_order[index: index + num_of_children]
        for child in child_data:
            child_node = TreeNode(child)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root


def main():
    root = take_input_levelwise()
    res = leaf_node(root)
    print(res)


main()

# Input: 10 3 20 30 40 2 40 50 0 0 0 0 
# Output: 4