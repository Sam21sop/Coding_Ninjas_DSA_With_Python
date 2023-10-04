


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None
        self.nodes_count = 0

    def insert_helper(self, root, data):
        if root is None:
            return TreeNode(data)
        if root.data >= data:
            root.left = self.insert_helper(root.left, data)
            return root
        else:
            root.right = self.insert_helper(root.right, data)
            return root
        

    def insert(self, value):
        self.nodes_count += 1
        self.root = self.insert_helper(self.root, value)


    def is_present_helper(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        if root.data > key:
            return self.is_present_helper(root.left, key)
        return self.is_present_helper(root.right, key)


    def search(self, value):
        return self.is_present_helper(self.root, value)
    

    def min(self, root):
        if root is None:
            return 10000
        if root.left is None:
            return root.data
        return self.min(root.left)
    

    def delete_data_helper(self, root, data):
        if root is None:
            return False, None
        if root.data < data:
            deleted, new_right_node = self.delete_data_helper(root.right, data)
            root.right = new_right_node
            return deleted, root
        if root.left == None and root.right == None:
            return True, None
        if root.left is None:
            return True, root.right
        if root.right is None:
            return True, root.left
        replace = self.min(root.right)
        root.data = replace
        deleted, new_right_node = self.delete_data_helper(root.right, replace)
        root.right = new_right_node
        return True, root
    

    def delete(self, value):
        deleted, new_root = self.delete_data_helper(self.root, value)
        if deleted:
            self.nodes_count -= 1
        self.root = new_root
        return deleted
    

    def count(self):
        return self.nodes_count

    def display_tree_helper(self, root):
        '''Recursive'''
        if root is None:
            return
        print(root.data, end=':')
        if root.left != None:
            print('L:', root.left.data, sep='', end=',')
        if root.right != None:
            print('R:', root.right.data, sep='', end=' ')
        print()
        self.display_tree_helper(root.left)
        self.display_tree_helper(root.right)


    def display(self):
        self.display_tree_helper(self.root)


def main():
    b = BST()
    q = int(input())
    while q > 0:
        li = [int(i) for i in input().strip().split()]
        # print("1.Insert 2.Delete 3.Search 4.Display")
        choice = li[0]
        q -= 1
        if choice == 1:
            data = li[1]
            b.insert(data)
        elif choice == 2:
            data = li[1]
            b.delete(data)
        elif choice == 3:
            data = li[1]
            ans = b.search(data)
            if ans:
                print('true')
            else:
                print('false')
        elif choice == 4:
            b.display()
        else:
            print('Invalid Input')

if __name__ == '__main__':
    main()

# 6
# 1 2
# 1 3
# 1 1
# 4
# 2 2
# 4