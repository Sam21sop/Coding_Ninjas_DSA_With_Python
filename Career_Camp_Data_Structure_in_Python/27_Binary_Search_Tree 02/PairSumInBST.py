from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def pair_sum(sorted_list, target:int):
    left = 0
    right = len(sorted_list) - 1
    pairs = []
    while left < right:
        current_sum = sorted_list[left] + sorted_list[right]
        if current_sum == target:
            pairs.append((sorted_list[left], sorted_list[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs


def inorder_traversal(root:TreeNode, lst:[]):
    if root is None:
        return
    inorder_traversal(root.left, lst)
    lst.append(root.data)
    inorder_traversal(root.right, lst)


def display_nodes_sum(root:TreeNode, target:int):
    inorder_lst = []
    inorder_traversal(root, inorder_lst)
    sum_pairs = pair_sum(inorder_lst, target)
    for pair in sum_pairs:
        print(pair[0], pair[1])


def build_level_order_tree(level_order:list[int]):
    ''''''
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


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_level_order_tree(level_order)
    s = int(input())
    display_nodes_sum(root, s)


main()

# Input:
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 12

# Output:
# 2 10
# 5 7