from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    # Check if the current node's data is within the valid range
    if root.data <= min_val or root.data >= max_val:
        return False

    # Recursively check the left and right subtrees
    return (isBST(root.left, min_val, root.data) and isBST(root.right, root.data, max_val))


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
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
        #build right subtree
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_root.right = right_node
            q.put(right_node)
    return root


def main():
    root = take_input()
    result = isBST(root)
    print(result)


if __name__ == '__main__':
    main()
    

# input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1