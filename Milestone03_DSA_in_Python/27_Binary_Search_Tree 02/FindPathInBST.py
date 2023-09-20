from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def find_path_in_BST(root, target):
    if root is None:
        return
    if target == root.data:
        output = []
        output.append(root.data)
        return output
    elif target < root.data:
        output = find_path_in_BST(root.left, target)
        if output is not None:
            output.append(root.data)
        return output
    else:
        output = find_path_in_BST(root.right, target)
        if output is not None:
            output.append(root.data)
        return output
    

def build_level_order_tree(level_order):
    index = 0
    if len(level_order) <= 0 or level_order[0] == -1:
        return
    root = TreeNode(level_order[index])
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        current_root = q.get()
        left_child_data = level_order[index]
        index += 1
        if left_child_data != -1:
            left_node = TreeNode(left_child_data)
            current_root.left = left_node
            q.put(left_node)
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_root.right = right_node
            q.put(right_node)
    return root


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_level_order_tree(level_order)
    target = int(input())
    path = find_path_in_BST(root, target)
    if path is not None:
        print(*path, end=" ")


if __name__ == '__main__':
    main()