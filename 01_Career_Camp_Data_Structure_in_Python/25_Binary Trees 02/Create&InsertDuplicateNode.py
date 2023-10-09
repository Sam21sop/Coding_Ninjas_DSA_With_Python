'''
TimeComplexity: O(n)
SpaceComplexity: O(H) => logn
'''

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def insert_duplicate_node(root):
    if root is None:
        return
    new_node = TreeNode(root.data)              #create new node

    current_root_left = root.left               #swap old node with new node
    root.left = new_node
    new_node.left = current_root_left

    insert_duplicate_node(current_root_left)
    insert_duplicate_node(root.right)


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
        left_child = level_order[index]
        index += 1
        if left_child != -1:
            left_node = TreeNode(left_child)
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


def display_level_wise(root):
    if root is None:
        return
    input_queue = Queue()
    output_queue = Queue()
    
    input_queue.put(root)
    while not input_queue.empty():
        while not input_queue.empty():
            curr = input_queue.get()
            print(curr.data, end=' ')
            if curr.left != None:
                output_queue.put(curr.left)
            if curr.right != None:
                output_queue.put(curr.right)
        print()
        input_queue, output_queue = output_queue, input_queue
    

def main():
    root = take_input()
    insert_duplicate_node(root)
    display_level_wise(root)


if __name__ == '__main__':
    main()


# Input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# Output:
# 8 
# 8 10
# 5 10
# 5 6
# 2 6 7
# 2 7