from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def tree_height(root):
    if root is None:
        return 0
    left_subtree_height = tree_height(root.left)
    right_subtree_height = tree_height(root.right)
    return 1 + max(left_subtree_height, right_subtree_height)


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    start = 0
    
    length = len(level_order)
    if length == 1:
        return None
    
    root = TreeNode(level_order[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()

        #build left subtree
        left_child = level_order[start]
        start += 1
        if left_child != -1:
            left_subtree_root = TreeNode(left_child)
            current_node.left = left_subtree_root
            q.put(left_subtree_root)

        #build right subtree
        right_child = level_order[start]
        start += 1
        if right_child != -1:
            right_subtree_root = TreeNode(right_child)
            current_node.right = right_subtree_root
            q.put(right_subtree_root)
        
    return root
    

def main():
    root = take_input()
    h = tree_height(root)
    print(h)

if __name__ == '__main__':
    main()

# 10 20 30 40 50 -1 -1 -1 -1 -1 -1