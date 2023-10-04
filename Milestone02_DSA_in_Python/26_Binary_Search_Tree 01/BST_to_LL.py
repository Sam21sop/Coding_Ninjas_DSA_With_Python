'''
TimeComplexity: O()
SpaceComplexity: O()
'''

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def build_level_order_tree(level_order):
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


def linked_list_from_bst(root):
    if root is None:
        return None
    lst = linked_list_from_bst(root.left)
    current = Node(root.data)
    current.next = linked_list_from_bst(root.right)
    if lst == None:
        return current
    pointer = lst
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = current
    return lst


def display_linked_list(head):
    current = head
    while current != None:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    level_order = [int(i) for i in input().strip().split()]
    root = build_level_order_tree(level_order)
    head = linked_list_from_bst(root)
    display_linked_list(head)


if __name__ == '__main__':
    main()


# Input: 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1 
# Output: 2 5 6 7 8 10