from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def replace_with_larger_node_sum_helper(root, total_sum):
    if root == None:
        return total_sum
    total_sum = replace_with_larger_node_sum_helper(root.right, total_sum)
    total_sum += root.data
    root.data = total_sum
    total_sum = replace_with_larger_node_sum_helper(root.left, total_sum)
    return total_sum


def replace_with_larger_node_sum(root):
    total_sum = 0
    replace_with_larger_node_sum_helper(root, total_sum)


def build_tree(level_order):
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


def display_levelwise_at_diff_level(root):
    if root is None:
        return 
    q = Queue()
    q.put(root)
    q.put(None)
    while not q.empty():
        front_node = q.get()
        if front_node is None:
            if q.empty():
                break
            print()
            q.put(None)
            continue
        print(front_node.data, end=' ')
        if front_node.left != None:
            q.put(front_node.left)
        if front_node.right != None:
            q.put(front_node.right)


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_tree(level_order)
    replace_with_larger_node_sum(root)
    display_levelwise_at_diff_level(root)


if __name__ == '__main__':
    main()
