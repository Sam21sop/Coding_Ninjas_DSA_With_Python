from GenericTree import TreeNode

#create nodes 
n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(9)
n4 = TreeNode(8)
n5 = TreeNode(15)
n6 = TreeNode(1)
n7 = TreeNode(7)


n1.childrens.extend([n1, n2, n3, n4, n5])     # add childer for node 5

n3.childrens.extend([n6, n7])                 #add children of node 3

