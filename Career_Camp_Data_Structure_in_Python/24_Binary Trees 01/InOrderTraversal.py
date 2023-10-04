from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    start = 0

    root = TreeNode(level_order[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current_root = q.get()

        #build left subtree
        left_child = level_order[start]
        start += 1
        if left_child != -1:
            left_subtree_root = TreeNode(left_child)
            current_root.left = left_subtree_root
            q.put(left_subtree_root)

        #build right subtree
        right_child = level_order[start]
        start += 1
        if right_child != -1:
            right_subtree_root = TreeNode(right_child)
            current_root.right = right_subtree_root
            q.put(right_subtree_root)

    return root


def main():
    root = take_input()
    in_order(root)

if __name__ == '__main__':
    main()

# Input: 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Output: 4 2 5 1 6 3 7

# INput: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# Output: 7 3 8 1 9 4 10 0 11 5 12 2 13 6 14 