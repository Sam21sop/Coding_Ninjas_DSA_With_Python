from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None


def take_input():
    '''Create Linked List from given Array/List
        Function will return head of linked list'''
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


def display(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    # print()


def main():
    head = take_input()
    display(head)


if __name__ == '__main__':
    main()