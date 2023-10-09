'''
Time Complexity: O(n)
Space Complexity: O(h)
'''
from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Pair:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


def diameter_helper(root):
    if root is None:
        return Pair(0, 0)
    
    left_pair = diameter_helper(root.left)
    right_pair = diameter_helper(root.right)

    left_diameter = left_pair.diameter
    right_diameter = right_pair.diameter

    diameter_from_root = left_pair.height + right_pair.height + 1

    diameter = max(left_diameter, right_diameter, diameter_from_root)
    height = max(left_pair.height, right_pair.height) + 1

    return Pair(diameter, height)


def diameter_of_tree(root):
    pair = diameter_helper(root)
    return pair.diameter


def diameterOfBinaryTree(root):
    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        max_diameter = max(max_diameter, left_depth + right_depth) 
        return max(left_depth, right_depth) + 1
    
    max_diameter = 0
    dfs(root)
    return max_diameter + 1


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
        current_node = q.get()

        #build left subtree
        left_child_value = level_order[index]
        index += 1
        if left_child_value != -1:
            left_node = TreeNode(left_child_value)
            current_node.left = left_node
            q.put(left_node)

        #build right subtree
        right_child_value = level_order[index]
        index += 1
        if right_child_value != -1:
            right_node = TreeNode(right_child_value)
            current_node.right = right_node
            q.put(right_node)
    return root


def display_level_wise(root):
    if root is None:
        return
    input_queue = Queue()
    output_queue = Queue()

    input_queue.put(root)
    while not input_queue.empty():
        while not input_queue.empty():
            current_node = input_queue.get()
            print(current_node.data, end=' ')
            if current_node.left != None:
                output_queue.put(current_node.left)
            if current_node.right != None:
                output_queue.put(current_node.right)
        print()
        input_queue, output_queue = output_queue, input_queue


def main():
    root = take_input()
    # display_level_wise(root)
    # print()
    # print(diameter_of_tree(root))
    print(diameterOfBinaryTree(root))


if __name__ == '__main__':
    main()