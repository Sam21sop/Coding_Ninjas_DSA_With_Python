from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def pre_order_traversal(root:TreeNode):
    if root is None:
        return
    print(root.data, end=' ')
    for child in root.children:
        pre_order_traversal(child)

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
        num_of_child = level_order[index]
        index += 1
        child_data = level_order[index: index+num_of_child]
        for child in child_data:
            node = TreeNode(child)
            current_node.children.append(node)
            q.put(node)
        index += num_of_child
    return root


def main():
    root = take_input_levelwise()
    pre_order_traversal(root)


main()