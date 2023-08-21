from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def insert_recursively(head, data, position):
    if position == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    else:
        head.next = insert_recursively(head.next, data, position-1)
        return head
    

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


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=' --> ')
        current = current.next
    print("None")

def main():
    head = take_input()
    head = insert_recursively(head, 99, 2)
    print_linked_list(head)


if __name__ == '__main__':
    main()    