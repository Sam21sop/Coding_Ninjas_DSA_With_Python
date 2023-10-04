from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def rev_recursively(head):
    if head is None:
        return
    rev_recursively(head.next)
    print(head.data, end=' ')

def take_input():
    head = None
    tail = None
    lst = list(map(int, stdin.readline().strip().split()))
    i = 0
    while i < len(lst) and lst[i] != -1:
        new_node = Node(lst[i])
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
        i += 1
    return head


def main():
    head = take_input()
    rev_recursively(head)

if __name__ == '__main__':
    main()