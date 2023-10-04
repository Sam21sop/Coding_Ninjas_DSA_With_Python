from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_tree_using_in_post(in_order, post_order):
    if not in_order or not post_order:
        return None
    
    root_data = post_order[-1]
    root = TreeNode(root_data)

    root_index = in_order.index(root_data)

    root.left = build_tree_using_in_post(in_order[:root_index], post_order[:root_index])
    root.right = build_tree_using_in_post(in_order[root_index+1: ], post_order[root_index: -1])

    return root


def display_level_wise(root):
    if root is None:
        return
    pending_nodes = Queue()
    pending_nodes.put(root)
    pending_nodes.put(None)

    while not pending_nodes.empty():
        front_node = pending_nodes.get()
        if front_node is None:
            print()
            if not pending_nodes.empty():
                pending_nodes.put(None)
        else:
            print(front_node.data, end=' ')
            if front_node.left is not None:
                pending_nodes.put(front_node.left)
            if front_node.right is not None:
                pending_nodes.put(front_node.right)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), list(), 0
    post_order = list(map(int, stdin.readline().strip().split()))
    in_order = list(map(int, stdin.readline().strip().split()))
    return in_order, post_order, n


def main():
    in_order, post_order, size = take_input()
    root = build_tree_using_in_post(in_order, post_order)
    display_level_wise(root)


if __name__ == '__main__':
    main()

# 7
# 4 5 2 6 7 3 1 
# 4 2 5 1 6 3 7 