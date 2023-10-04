from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    ''''''
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    ''''''
    if not root:
        return True
    if not min_val < root.data and root.data < max_val:
        return False
    return is_bst(root.left, min_val, root.data) and is_bst(root.right, root.data, max_val)


def get_bst_subtree_height(root):
    ''''''
    if not root:
        return 0
    if is_bst(root):
        return max(get_bst_subtree_height(root.left), get_bst_subtree_height(root.right)) + 1
    return max(get_bst_subtree_height(root.left), get_bst_subtree_height(root.right))


def largest_bst_subtree(root:TreeNode):
    ''''''
    return get_bst_subtree_height(root)


def build_level_order_tree(level_order:list[int]):
    ''''''
    index = 0
    if len(level_order) <= 0 or level_order[0] == -1:
        return None
    root = TreeNode(level_order[index])
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        left_child_data = level_order[index]
        index += 1
        if left_child_data != -1:
            left_node = TreeNode(left_child_data)
            current_node.left = left_node
            q.put(left_node)
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_node.right = right_node
            q.put(right_node)
    return root


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_level_order_tree(level_order)
    print(largest_bst_subtree(root))


main()

# Input: 5 10 6 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Output: 2