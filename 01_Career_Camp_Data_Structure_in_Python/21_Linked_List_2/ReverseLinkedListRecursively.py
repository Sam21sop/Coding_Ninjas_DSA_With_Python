from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


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
        print(current.data, end=" --> ")
        current = current.next
    print("None")


def main():
    head = take_input()
    head = reverse_linked_list(head)
    display_linked_list(head)


if __name__ == "__main__":
    main()