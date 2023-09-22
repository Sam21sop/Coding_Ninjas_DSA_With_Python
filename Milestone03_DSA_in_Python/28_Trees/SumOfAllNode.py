from queue import Queue


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def input_level_wise():
    li = [int(i) for i in input().strip().split()]
    index = 0
    data = li[index]
    index += 1
    if data == -1:
        return None
    root = TreeNode(data)
    q = Queue()
    q.put(root)
    while not q.empty():
        front_node = q.get()
        num_of_children = li[index]
        index += 1
        children_array = li[index: index + num_of_children]
        for child_data in children_array:
            child_node = TreeNode(child_data)
            front_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root


def sum_of_all_node(root):
    if root == None:
        return -1
    total_sum = root.data
    for child in root.children:
        total_sum += sum_of_all_node(child)
    return total_sum


def main():
    root = input_level_wise()
    res = sum_of_all_node(root)
    print(res)
    

main()