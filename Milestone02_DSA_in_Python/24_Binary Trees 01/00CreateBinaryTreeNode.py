class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(55)
root.left = TreeNode(50)
root.right = TreeNode(60)

print(root.data)
print(root.left.data)
print(root.right.data)
