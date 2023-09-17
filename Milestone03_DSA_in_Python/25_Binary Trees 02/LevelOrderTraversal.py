from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):
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
    level_order = list(map(int, stdin.readline().strip().split()))
    index = 0

    if len(level_order) == 1:
        return None
    
    root = TreeNode(level_order[index])
    index += 1
    q = Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()
        #build left subtree
        left_child_data = level_order[index]
        index += 1
        if left_child_data != -1:
            left_node = TreeNode(left_child_data)
            current_node.left = left_node
            q.put(left_node)
        #build right subtree
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_node.right = right_node
            q.put(right_node)
    return root


def main():
    root = take_input()
    level_order_traversal(root)


if __name__  == '__main__':
    main()


# Input: 10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1 
# Output:
# 10
# 20 30
# 40 50 60