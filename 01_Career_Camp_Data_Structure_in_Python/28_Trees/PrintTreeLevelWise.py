from queue import Queue


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


def take_input_levelwise():
    li = [int(i) for i in input().strip().split()]
    index = 0

    node_data = li[index]
    index += 1

    if node_data == -1:
        return None
    
    root = TreeNode(node_data)
    q = Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()
        num_of_children = li[index]
        index += 1
        children_array = li[index: index + num_of_children]
        for child_data in children_array:
            child_node = TreeNode(child_data)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root


def display_levelwise(root):
    if root is None:
        return
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            print(node.data, end=' ')
            for child in node.children:
                queue.append(child)
        print()


def main():
    root = take_input_levelwise()
    display_levelwise(root)


main()