class TreeNode:
    '''Binary tree node class'''
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_tree(perent_data:int, is_root:bool, is_left:bool):

    '''Build a tree from taking user input'''

    if is_root:
        print("Enter root data: ")
    else:
        if is_left:
            print('Enter left child of:', perent_data)
        else:
            print("Enter right child of:", perent_data)
    
    data = input()
    if data == '-1':                                                          # if root is -1 return None
        return None
    root = TreeNode(data)                                                   # create new tree node

    left_subtree_root = build_tree(data, False, True)                       # build left sub tree recursively
    right_subtree_root = build_tree(data, False, False)                     # buld right sub tree recursively

    root.left = left_subtree_root                                           # Attach left subtree to the root
    root.right = right_subtree_root                                         # Attach right subtree to the root

    return root


def display_tree(root):
    '''print the given tree in proper manner'''
    if root is None:
        return
    print(f'{root.data}: ', end='')
    if root.left is not None:                       #print left child if it is present
        print(f'L{root.left.data}, ', end='')
    if root.right is not None:                      #print right child if it is present
        print(f'R{root.right.data}', end='')
    print()

    display_tree(root.left)                         # Recursive call for left sub tree
    display_tree(root.right)                        # Recursive call for right sub tree


def main():
    root = build_tree(0, True, True)
    display_tree(root)


if __name__ == '__main__':
    main()