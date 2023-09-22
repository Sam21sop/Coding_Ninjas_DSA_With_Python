from GenericTree import TreeNode


# Create the root node
root = TreeNode("A")

# Add children to the root node
root.add_child(TreeNode("B"))
root.add_child(TreeNode("C"))
root.add_child(TreeNode("D"))

# Add children to node B
root.children[0].add_child(TreeNode("E"))
root.children[0].add_child(TreeNode("F"))

# Add children to node D
root.children[2].add_child(TreeNode("G"))
root.children[2].add_child(TreeNode("H"))

# Add children to node E
root.children[0].children[0].add_child(TreeNode("I"))
root.children[0].children[0].add_child(TreeNode("J"))


#print tree recursively
root.display()