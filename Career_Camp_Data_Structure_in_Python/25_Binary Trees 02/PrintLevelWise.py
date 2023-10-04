from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def print_level_wise(root):
    if root is None:
        return
    data_queue = [root]
    while data_queue:
        current_node = data_queue.pop(0)
        left_child_data = current_node.left.data if current_node.left else -1
        right_child_data = current_node.right.data if current_node.right else -1
        print('{}:L:{},R:{}'.format(current_node.data, left_child_data, right_child_data))
        if current_node.left:
            data_queue.append(current_node.left)
        if current_node.right:
            data_queue.append(current_node.right)
        

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
            right_child = TreeNode(right_child_value)
            current_node.right = right_child
            q.put(right_child)
    return root


def main():
    root = take_input()
    print_level_wise(root)


if __name__ == '__main__':
    main()