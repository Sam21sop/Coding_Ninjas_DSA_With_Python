from sys import stdin, setrecursionlimit

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


def bubble_sort(head):
    if not head or not head.next:
        return head
    swapped = True
    while swapped:
        swapped = False
        current = head
        while current.next:
            if current.data > current.next.data:
                swapped = True
                temp = current.data
                current.data = current.next.data
                current.next.data = temp
            current = current.next
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
    sorted_linked_list = bubble_sort(head)
    display_linked_list(sorted_linked_list)


if __name__ == '__main__':
    main()