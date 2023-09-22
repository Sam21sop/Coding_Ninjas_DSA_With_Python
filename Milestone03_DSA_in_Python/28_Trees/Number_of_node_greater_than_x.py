from queue import Queue


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def take_input_levelwise(level_order):
    index = 0
    
    node_data = level_order[index]
    index += 1
    if node_data == -1:
        return None
    
    root = TreeNode(node_data)
    q = Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()
        num_of_children = level_order[index]
        index += 1
        children_array = level_order[index: index + num_of_children]
        for child_data in children_array:
            child_node = TreeNode(child_data)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root

def num_nodes_gt_x(root, x):
    if root is None:
        return 0
    count = 0
    if root.data > x:
        count += 1
    for child in root.children:
        count += num_nodes_gt_x(child, x)
    return count  


def main():
    level_order = [int(i) for i in input().strip().split()]
    x = level_order[0]
    root = take_input_levelwise(level_order[1:])
    res = num_nodes_gt_x(root, x)
    print(res)


main()

# Input: 10 10 3 20 30 40 2 40 50 0 0 0 0 
# Output: 5