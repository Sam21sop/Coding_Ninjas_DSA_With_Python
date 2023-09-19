from sys import stdin,setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def lowest_common_anscester_helper(root, value1, value2):
    if root is None or root.data == value1 or root.data == value2:
        return root
    
    if root.data < value1 and root.data < value2:
        return lowest_common_anscester_helper(root.right, value1, value2)
    
    if root.data > value1 and root.data > value2:
        return lowest_common_anscester_helper(root.left, value1, value2)
    
    left_lca = lowest_common_anscester_helper(root.left, value1, value2)
    right_lca = lowest_common_anscester_helper(root.right, value1, value2)
    
    if left_lca != None and right_lca != None:
        return root
    elif left_lca != None:
        return left_lca
    return right_lca


def lowest_common_anscester(root, value1, value2):
    node = lowest_common_anscester_helper(root, value1, value2)
    return -1 if (node == None) else node.data

def build_level_tree(level_order):
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


def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)
    


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_level_tree(level_order)
    # pre_order(root)
    # print()
    k1, k2 = (int(i) for i in input().strip().split())
    result = lowest_common_anscester(root, k1, k2)
    print(result)


if __name__ == '__main__':
    main()