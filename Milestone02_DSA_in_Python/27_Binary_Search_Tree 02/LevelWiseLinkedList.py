from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def build_level_order_tree(level_order:list[int]):
    index = 0
    if len(level_order) <= 0 or level_order[0] == -1:
        return None
    root = TreeNode(level_order[index])
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        left_child_data = level_order[index]
        index += 1
        if left_child_data != -1:
            left_node = TreeNode(left_child_data)
            current_node.left = left_node
            q.put(left_node)
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_node.right = right_node
            q.put(right_node)
    return root


def build_linked_list_for_each_level(root:TreeNode):
    if root is None:
        return []
    result = []
    current_level_nodes = [root]                        # creating list for current level
    while current_level_nodes:                          # iterate over current level order list
        next_level_nodes = []                           # create empty list for storing next level nodes
        temp_levelwise_head = ListNode(None)            # creating temp head for each level
        current_node = temp_levelwise_head              
        for node in current_level_nodes:                #iterate over level order for creating linked list of each level 
            current_node.next = ListNode(node.data)     #creating linked list node
            current_node = current_node.next            
            if node.left:                               
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        result.append(temp_levelwise_head.next)
        current_level_nodes = next_level_nodes
    return result


def display_linked_list(head:ListNode):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_level_order_tree(level_order)
    output_list = build_linked_list_for_each_level(root)
    if output_list is not None:
        for head in output_list:
            display_linked_list(head)


main()