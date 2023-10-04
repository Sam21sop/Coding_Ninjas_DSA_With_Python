from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def tree_to_depth_tree(root, depth=0):
    if root is None:
        return
    root.data = depth
    tree_to_depth_tree(root.left, depth + 1)
    tree_to_depth_tree(root.right, depth + 1)


def take_input():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)
    if length == 1 :
        return None
    
    root = TreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = TreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = TreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)


def main():
    root = take_input()
    tree_to_depth_tree(root)
    in_order(root)


if __name__ == '__main__':
    main()

# input: 2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1 -1 
# output: 2 1 2 0 2 1 2 