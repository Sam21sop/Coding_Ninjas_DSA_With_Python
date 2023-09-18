from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def construct_bst(arr_lst):
    if not arr_lst:
        return None
    
    mid_index = (len(arr_lst)-1) // 2
    root = TreeNode(arr_lst[mid_index])
    root.left = construct_bst(arr_lst[:mid_index])
    root.right = construct_bst(arr_lst[mid_index+1:])
    return root


def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def main():
    n=int(input())
    if(n>0):
        lst = [int(i) for i in input().strip().split()]
    else:
        lst = []
    root = construct_bst(lst)
    pre_order(root)

if __name__ == '__main__':
    main()


# 7
# 1 2 3 4 5 6 7