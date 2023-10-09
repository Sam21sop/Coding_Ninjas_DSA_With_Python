class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return
    
    print(f"{root.data}:", end='')
    if root.left is not None:
        print(f'L{root.left.data}, ', end='')
    if root.right is not None:
        print(f'R{root.right.data}', end='')
    print()

    print_tree(root.left)
    print_tree(root.right)

def main():
    root = TreeNode(1)
    
    root_left = TreeNode(2)
    root_right = TreeNode(3)
    
    root.left = root_left
    root.right = root_right

    two_right = TreeNode(4)
    two_left = TreeNode(5)

    root_left.left = two_left
    root_right.right = two_right

    print_tree(root)


if __name__ == '__main__':
    main()