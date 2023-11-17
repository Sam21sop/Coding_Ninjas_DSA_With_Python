from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def mergeBST(root1, root2):
    def inorderTraversal(root, result):
        if root:
            inorderTraversal(root.left, result)
            result.append(root.data)
            inorderTraversal(root.right, result)
    
    def sortedArrayToBST(arr, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(arr[mid])
        node.left = sortedArrayToBST(arr, left, mid-1)
        node.right = sortedArrayToBST(arr, mid+1, right)
        return node
    element1, element2 = [], []
    inorderTraversal(root1, element1)
    inorderTraversal(root2, element2)
    merged_element = []
    i, j = 0, 0
    while i < len(element1) and j < len(element2):
        if element1[i] < element2[j]:
            merged_element.append(element1[i])
            i += 1
        else:
            merged_element.append(element2[i])
            j += 1
    while i < len(element1):
        merged_element.append(element1[i])
        i += 1
    while j < len(element2):
        merged_element.append(element2[j])
        j += 1
    return sortedArrayToBST(merged_element, 0, len(merged_element) - 1)


def build_level_order_tree(level_order):
    index = 0
    if len(level_order) <= 0 or level_order[0] == -1:
        return
    root = TreeNode(level_order[index])
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        current_root = q.get()
        left_child_data = level_order[index]
        index += 1
        if left_child_data != -1:
            left_node = TreeNode(left_child_data)
            current_root.left = left_node
            q.put(left_node)
        right_child_data = level_order[index]
        index += 1
        if right_child_data != -1:
            right_node = TreeNode(right_child_data)
            current_root.right = right_node
            q.put(right_node)
    return root


def display_tree(root):
    if root is None:
        return
    display_tree(root.left)
    print(root.data end=' ')
    display_tree(root.right)


def main():
    level_order1 = list(map(int, stdin.readline().strip().split()))
    tree1 = build_level_order_tree(level_order1)
    level_order2 = list(map(int, stdin.readline().strip().split()))
    tree12 = build_level_order_tree(level_order2)
    new_root = mergeBST(tree1, tree12)
    display_tree(new_root)


if __name__ == '__main__':
    main()