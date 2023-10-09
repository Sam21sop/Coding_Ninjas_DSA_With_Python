from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    
def BST(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return BST(root.left, key)
    return BST(root.right, key)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = TreeNode(levelorder[index])
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        #build left subtree
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = TreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        #build right subtree
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = TreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root


def main():
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    k = int(input())
    ans = BST(root, k)
    if ans:
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    main()


# Input: 
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 2
# Output: true