'''
Time Complexity: O(n)
Space Complexity: O(h)
'''

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def node_at_k_diastance_down(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    node_at_k_diastance_down(root.left, k-1)
    node_at_k_diastance_down(root.right, k-1)


def node_distance_k_helper(root, target, k):
    if root is None:
        return -1
    if root.data == target:
        node_at_k_diastance_down(root, k)
        return 0
    
    left_data = node_distance_k_helper(root.left, target, k)
    if left_data != -1:
        if left_data + 1 == k:
            print(root.data)
        else:
            node_at_k_diastance_down(root.right, k - left_data - 2)
        return 1 + left_data
    
    right_data = node_distance_k_helper(root.right, target, k)
    if right_data != -1:
        if right_data + 1 == k:
            print(root.data)
        else:
            node_at_k_diastance_down(root.left, k - right_data - 2)
        return 1 + right_data
    return -1


def node_at_distance_k(root, node, k):
    node_distance_k_helper(root, node, k)


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    index = 0
    if len(level_order) == 1:
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
    target_k = stdin.readline().strip().split()
    target = int(target_k[0])
    k = int(target_k[1])
    node_at_distance_k(root, target, k)


if __name__ == '__main__':
    main()


# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 3 1