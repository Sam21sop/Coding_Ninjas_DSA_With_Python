from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def is_structurally_identical(root1, root2):
    if root1 is None and root2 is None:                     #base condition
        return True
    
    elif root1 is None or root2 is None:                    # return false if any one root is null
        return False
    
    if len(root1.children) != len(root2.children):          # return false if length of children not equal
        return False
    
    for child1, child2 in zip(root1.children, root2.children):
        if not is_structurally_identical(child1, child2):           #recursive call on children
            return False
    return True


def take_input_levelwise():
    level_order = list(map(int, stdin.readline().strip().split()))
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
        num_of_children = level_order[index]
        index += 1
        children_node_data = level_order[index : index + num_of_children]
        for child in children_node_data:
            child_node = TreeNode(child)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root


def main():
    root1 = take_input_levelwise()
    root2 = take_input_levelwise()
    if is_structurally_identical(root1, root2):
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()


# Input:
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 20 30 40 2 40 50 0 0 0 0

# Output: true