from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    
def remove_leaf_node(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = remove_leaf_node(root.left)
    root.right = remove_leaf_node(root.right)
    return root


def take_input(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order.pop(0))
    queue = [root]
    while queue:
        current = queue.pop(0)
        if level_order:
            left_value = level_order.pop(0)
            if left_value != -1:
                current.left = TreeNode(left_value)
                queue.append(current.left)
        if level_order:
            right_value = level_order.pop(0)
            if right_value != -1:
                current.right = TreeNode(right_value)
                queue.append(current.right)
    return root


def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=' ')


def main():
    level_order = list(map(int, input().strip().split()))
    root = take_input(level_order)
    new_root = remove_leaf_node(root)
    pre_order(new_root)
    print()
    in_order(new_root)
    print()
    post_order(new_root)
    print()


if __name__ == '__main__':
    main()