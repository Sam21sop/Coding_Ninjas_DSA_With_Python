from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10 ** 6)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countNodesGreaterThanX(root, x) :
    if root is None:
        return 0
    stack = []
    current = root
    count = 0
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            if current.data > x:
                count += 1
            current = current.right

    return count


def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        #build right subtree
        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        
        #build left subtree
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root


def main():
    root = takeInput()
    x = int(stdin.readline().strip())

    count = countNodesGreaterThanX(root, x)
    print(count)


if __name__ == '__main__':
    main()

# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# 0