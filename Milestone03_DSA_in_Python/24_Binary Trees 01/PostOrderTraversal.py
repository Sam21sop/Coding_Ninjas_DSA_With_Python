from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=' ')


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    start = 0
    lenght = len(level_order)
    root = TreeNode(level_order[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_root = q.get()

        #build left subtree
        left_subtree_child = level_order[start]
        start += 1
        if left_subtree_child != -1:
            left_node = TreeNode(left_subtree_child)
            current_root.left = left_node
            q.put(left_node)

        #build right subtree
        right_subtree_child = level_order[start]
        start += 1
        if right_subtree_child != -1:
            right_node = TreeNode(right_subtree_child)
            current_root.right = right_node
            q.put(right_node)
    return root


def main():
    root = take_input()
    post_order(root)

if __name__ == '__main__':
    main()

# input: 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# output: 4 5 2 6 7 3 1