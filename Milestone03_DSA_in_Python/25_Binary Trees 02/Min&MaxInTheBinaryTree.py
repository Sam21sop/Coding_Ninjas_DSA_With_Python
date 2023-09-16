'''
Time Complexity: O(n)
Space Complexity: O(h)
'''

from sys import stdin, setrecursionlimit
from queue import Queue

setrecursionlimit(10**6)
Maximum = float('-inf')     #-9999999999
Minimum = float('inf')      #9999999999

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Pair:
    def __init__(self, maximum, minimum):
        self.minimum = minimum
        self.maximum = maximum


def get_min_max(root):
    if root is None:
        return Pair(Maximum, Minimum)
    
    left_pair = get_min_max(root.left)
    right_pair = get_min_max(root.right)

    minimum = min(root.data, left_pair.minimum, right_pair.minimum)
    maximum = max(root.data, left_pair.maximum, right_pair.maximum)
    return Pair(maximum, minimum)


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
    pair = get_min_max(root)
    print('{} {}'.format(pair.minimum, pair.maximum))


if __name__ == '__main__':
    main()