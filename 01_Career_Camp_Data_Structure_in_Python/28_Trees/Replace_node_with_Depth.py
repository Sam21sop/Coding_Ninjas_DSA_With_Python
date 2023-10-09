from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def replace_node_with_depth(root):
    level = 0
    q = Queue()
    q.put(root)
    q.put(None)
    
    while not q.empty():
        front_node = q.get()
        if front_node is None:
            if q.empty():
                break
            level += 1
            q.put(None)
        else:
            front_node.data = level
            for i in range(len(front_node.children)):
                q.put(front_node.children[i])


def build_tree(level_order):
    data = level_order.pop(0)
    root = TreeNode(data)
    q = [root]
    while q:
        current_node = q.pop(0)
        num_of_children = level_order.pop(0)
        for _ in range(num_of_children):
            child_data = level_order.pop(0)
            node = TreeNode(child_data)
            current_node.children.append(node)
            q.append(node)
    return root


def display_levelwise(root):
    if root is None:
        return
    q = [root]
    while q:
        for _ in range(len(q)):
            node = q.pop(0)
            print(node.data, end=' ')
            for child in node.children:
                q.append(child)
        print()


def main():
    level_order = list(map(int, stdin.readline().strip().split()))
    root = build_tree(level_order)
    replace_node_with_depth(root)
    display_levelwise(root)


if __name__ == '__main__':
    main()


# Input: 
# 1 1 2 2 30 4 1 5 1 60 1 70 1 8 1 9 1 100 0 0

# Output:
# 0   
# 1   
# 2 2 
# 3 3 
# 4 4 
# 5 5 