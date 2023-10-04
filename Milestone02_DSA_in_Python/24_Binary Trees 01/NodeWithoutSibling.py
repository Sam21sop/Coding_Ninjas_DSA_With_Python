from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def node_without_sibling(root):
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data, end=' ')
    elif root.right is not None and root.left is None:
        print(root.right.data, end=' ')

    node_without_sibling(root.left)
    node_without_sibling(root.right)


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


def main():
    root = take_input()
    node_without_sibling(root)


if __name__ == '__main__':
    main()


# input: 1 4 5 6 -1 -1 7 20 30 80 90 -1 -1 -1 -1 -1 -1 -1 -1
# output: 6 7