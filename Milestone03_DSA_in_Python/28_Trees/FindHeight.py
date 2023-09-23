from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def tree_height(root:TreeNode):
    if root is None:
        return 0
    height = 0
    for child in root.children:
        child_height = tree_height(child)
        if child_height > height:
            height = child_height
    return height + 1                           # add 1 for root node count


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
        children_data = level_order[index: index + num_of_children]
        for child in children_data:
            child_node = TreeNode(child)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root


def main():
    root = take_input_levelwise()
    h = tree_height(root)
    print(h)


if __name__ == '__main__':
    main()


# Input: 10 3 20 30 40 2 40 50 0 0 0 0 
# Output: 3