from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def find_second_largest(root):
    if len(root.children) == 0:
        return
    
    first_larget = root
    second_largest = None
    data = 0

    q = Queue()
    q.put(root)
    while not q.empty():
        front_node = q.get()
        for i in range(len(front_node.children)):
            q.put(front_node.children[i])
        if front_node.data > data:
            if front_node.data > first_larget.data:
                second_largest = first_larget
                data = first_larget.data
                first_larget = front_node
            elif front_node.data < first_larget.data:
                second_largest = front_node
                data = second_largest.data
    return second_largest


def take_input_levelwise():
    level_order = list(map(int, stdin.readline().strip().split()))
    index = 0

    data = level_order[index]
    index += 1
    if data == -1:
        return
    
    root = TreeNode(data)
    q = Queue()
    q.put(root)
    
    while not q.empty():
        current_node = q.get()
        num_of_children = level_order[index]
        index += 1
        child_data = level_order[index : index + num_of_children]
        for child in child_data:
            node = TreeNode(child)
            current_node.children.append(node)
            q.put(node)
        index += num_of_children
    return root


def main():
    root = take_input_levelwise()
    res = find_second_largest(root)
    print(res.data)


if __name__ == '__main__':
    main()


# Input: 10 3 20 30 40 2 40 50 0 0 0 0
# Output: 40