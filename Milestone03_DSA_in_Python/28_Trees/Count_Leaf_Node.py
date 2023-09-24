from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def count_leaf_node(root):
    if root is None:
        return 0
    if not root.children:
        return 1
    leaf_count = 0
    for child in root.children:
        leaf_count += count_leaf_node(child)
    return leaf_count


def build_tree_levelwise(level_order):
    data = level_order.pop(0)
    root = TreeNode(data)
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        num_of_children = level_order.pop(0)
        for child in range(num_of_children):
            child_data = level_order.pop(0)
            node = TreeNode(child_data)
            current_node.children.append(node)
            queue.append(node)
    return root


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_tree_levelwise(level_order)
    leaf_count = count_leaf_node(root)
    print(leaf_count)


if __name__ == '__main__':
    main()


# Input: 10 3 20 30 40 2 40 50 0 0 0 0 
# Output: 4