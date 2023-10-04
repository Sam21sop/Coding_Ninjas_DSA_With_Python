from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []




def is_present(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    for child in root.children:
        if is_present(child, x):
            return True
    return False


def take_input_levelwise(level_order):
    index = 0

    data = level_order[index]
    index += 1
    if data == -1:
        return None
    root = TreeNode(data)
    q = Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        num_of_child = level_order[index]
        index += 1
        child_data = level_order[index: index+num_of_child]
        for child in child_data:
            node = TreeNode(child)
            current_node.children.append(node)
            q.put(node)
        index += num_of_child
    return root


def main():
    key = int(input())
    level_order = list(map(int, stdin.readline().strip().split()))
    root = take_input_levelwise(level_order)
    res = is_present(root, key)
    if res:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()


# Input:
# 4
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 
# Output:
# false


# Input:
# 40
# 10 3 20 30 40 2 40 50 0 0 0 0 
#
# output:
# true