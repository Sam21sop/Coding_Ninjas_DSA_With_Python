from sys import stdin, setrecursionlimit

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def fun(start):
    if start is None:
        return
    print(start.data, end=' ')
    if start.next != None:
        fun(start.next.next)
    print(start.data, end=' ')

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


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=' --> ')
        current = current.next


def main():
    head = take_input()
    fun(head)

if __name__ == '__main__':
    main()