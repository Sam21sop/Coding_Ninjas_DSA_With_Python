from sys import stdin, setrecursionlimit

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def merge_two_sorted_linked_list(head1, head2):
    dummy = Node(0)
    current = dummy
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    if head1:
        current.next = head1
    if head2:
        current.next = head2
    return dummy.next


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
    print("None")

def main():
    t = int(input())
    while t > 0:
        head1 = take_input()
        head2 = take_input()
        new_head = merge_two_sorted_linked_list(head1, head2)
        display_linked_list(new_head)
        t -= 1


if __name__ == '__main__':
    main()


# 1
# 2 5 8 12 -1
# 3 6 9 -1