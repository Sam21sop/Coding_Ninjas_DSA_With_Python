from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def leaf_node(root):
    if root is None:
        return []
    
    leaf_node_lst = []

    def dfs(node):
        if node is not None:
            if node.left is None and node.right is None:
                leaf_node_lst.append(node.data)
            dfs(node.left)
            dfs(node.right)
    
    dfs(root)
    return leaf_node_lst


def take_input():
    level_order = list(map(int, stdin.readline().strip().split()))
    start = 0
    
    length = len(level_order)
    if length == 1:
        return None
    
    root = TreeNode(level_order[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()

        #build left subtree
        left_child = level_order[start]
        start += 1
        if left_child != -1:
            left_subtree_root = TreeNode(left_child)
            current_node.left = left_subtree_root
            q.put(left_subtree_root)

        #build right subtree
        right_child = level_order[start]
        start += 1
        if right_child != -1:
            right_subtree_root = TreeNode(right_child)
            current_node.right = right_subtree_root
            q.put(right_subtree_root)
        
    return root

def main():
    root = take_input()
    ans = leaf_node(root)
    print(*ans)

if __name__ == '__main__':
    main()

# input: 10 20 30 40 50 -1 -1 -1 -1 -1 -1
# output: 40 50 30