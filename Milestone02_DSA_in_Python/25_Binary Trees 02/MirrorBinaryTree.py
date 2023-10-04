'''
Time Complexity: O(n)
Space Complexcity: O(h)
'''

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def mirror_binary_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror_binary_tree(root.right)
    mirror_binary_tree(root.right)
    return root


def take_input(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order.pop(0))
    queue = [root]

    while queue:
        current = queue.pop(0)
        if level_order:
            left_value = level_order.pop(0)
            if left_value != -1:
                current.left = TreeNode(left_value)
                queue.append(current.left)

        if level_order:
            right_value = level_order.pop(0)
            if right_value != -1:
                current.right = TreeNode(right_value)
                queue.append(current.right)
    return root


def display_level_wise(root):
    if root is None:
        return 
    input_queue = Queue()
    output_queue = Queue()
    
    input_queue.put(root)
    while not input_queue.empty():
        while not input_queue.empty():
            current = input_queue.get()
            print(current.data, end=' ')
            if current.left is not None:
                output_queue.put(current.left)
            if current.right is not None:
                output_queue.put(current.right)
        print()
        input_queue, output_queue = output_queue, input_queue
    

def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = take_input(level_order)
    new_root = mirror_binary_tree(root)
    display_level_wise(new_root)


if __name__ == '__main__':
    main()


# Input: 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Output:
        # 1 
        # 3 2
        # 6 7 4 5