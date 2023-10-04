from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def delete_recursively(head, position):
    if head is None:
        return 
    if position == 0:
        return head.next
    head.next = delete_recursively(head.next, position-1)
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


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    head = take_input()
    display_linked_list(head)
    head = delete_recursively(head, 2)
    display_linked_list(head)


if __name__ == '__main__':
    main()