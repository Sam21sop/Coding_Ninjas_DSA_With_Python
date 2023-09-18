from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def element_between_k1_k2(root, k1, k2):
    if root is None:
        return
    if k1 < root.data:
        element_between_k1_k2(root.left, k1, k2)
    if k1 <= root.data and root.data <= k2:
        print(root.data, end=' ')
    if k2 > root.data:
        element_between_k1_k2(root.right, k1, k2)


def build_tree(level_order):
    index = 0
    if len(level_order) <= 0 or level_order[0] == -1:
        return None
    root = TreeNode(level_order[index])
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        current_root = q.get()
        #build left subtree
        left_child_data = level_order[index]
        index += 1
        if left_child_data != -1:
            left_node = TreeNode(left_child_data)
            current_root.left = left_node
            q.put(left_node)
        #builf right subtree
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_root.right = right_node
            q.put(right_node)
    return root


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_tree(level_order)
    k1, k2 = (int(i) for i in input().strip().split())
    element_between_k1_k2(root, k1, k2)


if __name__ == '__main__':
    main()


# Input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# Output: 6 10