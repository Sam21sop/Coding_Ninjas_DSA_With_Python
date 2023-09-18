class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    # Check if the current node's value is within the valid range
    if root.value <= min_val or root.value >= max_val:
        return False

    # Recursively check the left and right subtrees
    return (isBST(root.left, min_val, root.value) and isBST(root.right, root.value, max_val))

# Example usage:
# Create a binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Check if it's a binary search tree
result = isBST(root)
print(result)