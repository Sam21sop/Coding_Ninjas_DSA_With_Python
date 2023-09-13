from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def is_node_present(root, x):
    if root is None:
        return False
    
    if root.data == x:
        return True
    
    return is_node_present(root.left, x) or is_node_present(root.right, x)


def build_level_tree(level_order):
    index = 0
    length = len(level_order)

    if length <= 0 or level_order[0] == -1:
        return None
    
    root = TreeNode(level_order[index])
    index += 1

    q = Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()
        #build left subtree
        left_child = level_order[index]
        index += 1
        if left_child != -1:
            left_node = TreeNode(left_child)
            current_node.left = left_node
            q.put(left_node)
        #build right subtree
        right_child = level_order[index]
        index += 1
        if right_child != -1:
            right_node = TreeNode(right_child)
            current_node.right = right_node
            q.put(right_node)
    return root


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_level_tree(level_order)
    x = int(input())
    ans = is_node_present(root, x)
    if ans:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()

# Input: 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Output: 7