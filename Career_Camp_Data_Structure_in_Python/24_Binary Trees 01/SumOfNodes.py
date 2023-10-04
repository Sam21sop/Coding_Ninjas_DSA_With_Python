'''
Time complexity: O(N)       # N number of node in the tree
Space complexity: O(H)      # H is height of the input tree
'''
from sys import stdin,setrecursionlimit
import queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def get_sum(root):
    if root is None:
        return 0
    left_subtree_sum = get_sum(root.left)
    right_subtree_sum = get_sum(root.right)
    return (left_subtree_sum + right_subtree_sum) + root.data

def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    start = 0
    lenght = len(level_order)
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
    r = take_input()
    res = get_sum(r)
    print(res)


if __name__ == '__main__':
    main()