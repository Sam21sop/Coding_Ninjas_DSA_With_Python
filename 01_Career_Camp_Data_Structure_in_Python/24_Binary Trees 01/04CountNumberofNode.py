class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def count_node(root):
    if root is None:
        return 0
    
    left_subtree_count = count_node(root.left)
    right_subtree_count = count_node(root.right)
    return 1 + left_subtree_count + right_subtree_count


def take_input(parent_data:int, is_root:bool, is_left:bool):
    if is_root:
        print("Enter root data: ", end='')
    else:
        if is_left:
            print('Enter left child of:', parent_data)
        else:
            print('Enter right child of:', parent_data)
    data = input()
    if data == '-1':
        return
    root = TreeNode(data)
    left_subtree_root = take_input(data, False, True)
    right_subtree_root = take_input(data, False, False)

    root.left = left_subtree_root
    root.right = right_subtree_root

    return root


def display_tree(root):
    if root is None:
        return
    
    print(f"{root.data}:", end='')
    if root.left is not None:
        print(f"L{root.left.data}, ", end='')
    if root.right is not None:
        print(f'R{root.right.data}', end='')
    print()

    display_tree(root.left)
    display_tree(root.right)


def main():
    root = take_input()
    result = count_node(root)
    print(result)


if __name__ == "__main__":
    main()