from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


class PairSum:
    def __init__(self) -> None:
        self.node = None
        self.total_sum = float('-inf')


def max_sum_node_helper(root):
    if root is None:
        pair = PairSum()
        return pair
    
    t_sum = root.data
    for child in root.children:
        t_sum += child.data
    
    ans = PairSum()
    ans.node = root
    ans.total_sum = t_sum

    for child in root.children:
        child_ans = max_sum_node_helper(child)
        if child_ans.total_sum > ans.total_sum:
            ans = child_ans
    
    return ans


def max_sum_node(root:TreeNode):
    return max_sum_node_helper(root).node


def take_input_levelwise(level_order:[int]):
    index = 0
    data = level_order[index]
    if data == -1:
        return None
    root = TreeNode(data)
    index += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        num_of_children = level_order[index]
        index += 1
        child_data = level_order[index: index + num_of_children]
        for child in child_data:
            child_node = TreeNode(child)
            current_node.children.append(child_node)
            q.put(child_node)
        index += num_of_children
    return root


def main():
    level_order = [int(i) for i in input().strip().split()]
    root = take_input_levelwise(level_order)
    result = max_sum_node(root)
    if result is None:
        print(float('-inf'))
    else:
        print(result.data)


if __name__ == '__main__':
    main()


# Input: 5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0
# Output: 1