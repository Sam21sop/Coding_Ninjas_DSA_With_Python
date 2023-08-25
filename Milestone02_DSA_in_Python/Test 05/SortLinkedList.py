from sys import stdin, setrecursionlimit

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthLL(head):
    count = 1
    curr = head
    while curr.next != None:
        curr = curr.next
        count += 1
    return count


def sortList(head):
    if head is None or head.next is None:
        return head
    for i in range(lengthLL(head)-1):
        curr = head
        prev = None
        next = curr.next
        while curr.next != None:
            if curr.data > curr.next.data:
                if prev is None:
                    curr.next = next.next
                    next.next = curr
                    head = prev
                else:
                    next = curr.next
                    curr.next = next.next
                    prev.next = next
                    next.next = curr
                    prev = next
            else:
                prev = curr
                curr = curr.next
    return head


def take_input():
    head = None
    tail = None
    lst = list(map(int, input().split()))
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


def show_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    head = take_input()
    sorted_linked_list = sortList(head)
    show_linked_list(sorted_linked_list)

main()