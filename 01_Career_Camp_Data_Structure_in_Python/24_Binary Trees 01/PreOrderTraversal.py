from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    start = 0
    length = len(level_order)
    root = TreeNode(level_order[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        
        left_child = level_order[start]
        start += 1
        if left_child != -1:
            left_node = TreeNode(left_child)
            current_node.left = left_node
            q.put(left_node)
        
        right_child = level_order[start]
        start += 1
        if right_child != -1:
            right_node = TreeNode(right_child)
            current_node.right = right_node
            q.put(right_node)
    return root


def main():
    root = take_input()
    pre_order(root)


if __name__ == '__main__':
    main()

# input:1 2 3 5 4 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# output: 1 2 5 4 3 6 7