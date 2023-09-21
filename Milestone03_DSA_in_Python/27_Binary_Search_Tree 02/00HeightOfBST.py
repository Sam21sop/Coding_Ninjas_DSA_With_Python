from sys import stdin,setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def tree_height(root:TreeNode):
    if root is None:
        return 0                                #for node count
        #return -1                              #for edge count

    left_height = tree_height(root.left)        #recursive call on left subtree
    right_height = tree_height(root.right)      #recursive call on right subtree

    return 1 + max(left_height, right_height)   

def build_tree(level_order:list[int]):
    index = 0
    if len(level_order) <= 0 or level_order[0] == -1:
        return None
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
    root = build_tree(level_order)
    h = tree_height(root)
    print(h)


main()

# Input: 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Output: 4