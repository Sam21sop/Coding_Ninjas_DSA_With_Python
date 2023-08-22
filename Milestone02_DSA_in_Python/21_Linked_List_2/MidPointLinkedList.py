from sys import stdin

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def linked_list_mid_point(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def take_input():
    head = None
    tail = None
    lst = list(map(int, stdin.readline().strip().split()))
    i = 0
    while i < len(lst) and lst[i] != -1:
        new_head = Node(lst[i])
        if head is None:
            head = new_head
            tail = new_head
        else:
            tail.next = new_head
            tail = new_head
        i += 1
    return head


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=' --> ')
        current = current.next
    print('None')


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        head = take_input()
        mid_point = linked_list_mid_point(head)
        if mid_point:
            print(mid_point.data)
        t -= 1


if __name__ == '__main__':
    main()