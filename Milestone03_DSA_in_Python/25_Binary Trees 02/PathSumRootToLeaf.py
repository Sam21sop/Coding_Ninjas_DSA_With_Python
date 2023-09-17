'''
Time Complexity: O(n)
Space Complecity: O(h)
'''

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def path_sum_helper(root, k, path, curr_sum):
    if root is None:
        return
    if root.left is None and root.right is None:
        curr_sum += root.data
        if curr_sum == k:
            print(str(path + str(root.data)+" ").lstrip())
        return
    path_sum_helper(root.left, k, str(path + str(root.data) + " "), curr_sum + root.data)
    path_sum_helper(root.right, k, str(path + str(root.data) + " "), curr_sum + root.data)


def root_to_leaf_path_sum_to_k(root, k):
    path_sum_helper(root, k, "", 0)


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    index = 0

    if len(level_order) == 1:
        return
    
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
    k = int(stdin.readline().strip())
    root_to_leaf_path_sum_to_k(root, k)


if __name__ == '__main__':
    main()

# Input: 2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
# Output: 13