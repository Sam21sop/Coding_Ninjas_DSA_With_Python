from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_tree(preOrder, inOrder, n) :
	#Your code goes here
    if not preOrder or not inOrder:
        return None
    
    #the first element of preorder list is root
    root_data = preOrder[0]
    root = TreeNode(root_data)

    #lets Find the position position of root inOrder list
    root_index_inorder = inOrder.index(root_data)

    #lets construct left subtree and right subtree recursively
    root.left = build_tree(preOrder[1: 1+root_index_inorder], inOrder[ : root_index_inorder], n)
    root.right = build_tree(preOrder[1+root_index_inorder: ], inOrder[root_index_inorder+1: ], n)

    return root


def print_level_wise(root):
    if root is None :
        return
    pendingNodes = Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
        if frontNode is None :
            print()
            if not pendingNodes.empty() :
                pendingNodes.put(None)    
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


def take_input():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


def main():
    preOrder, inOrder, n = take_input()
    root = build_tree(preOrder, inOrder, n)
    print_level_wise(root)


if __name__ == '__main__':
    main()

# 7
# 1 2 4 5 3 6 7 
# 4 2 5 1 6 3 7 