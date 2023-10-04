from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    def __str__(self) -> str:
        return str(self.data)
    

def post_order_traversal(root:TreeNode):
    if root is None:
        return
    for child in root.children:
        post_order_traversal(child)
    print(root.data, end=' ')


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
        num_of_child = level_order[index]
        index += 1
        child_data = level_order[index: index + num_of_child]

        for child in child_data:
            child_node = TreeNode(child)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_child
    return root


def main():
    root =take_input_levelwise()
    post_order_traversal(root)


main()


# Input: 10 3 20 30 40 2 400 50 0 0 0 0 
# Output: 400 50 20 30 40 10