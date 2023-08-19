'''
Time complexity: O(n), where n is size of linked list 
Space Complexity: O(1)
'''

from sys import stdin, setrecursionlimit
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(head, position):
    if head is None:
        return None
    if position == 0:
        return head.next
    count = 0
    current = head
    while current is not None and count < position -1:
        count += 1
        current = current.next
    if current is None or current.next is None:
        return head
    current.next = current.next.next
    return head


def take_input():
    head = None
    tail = None
    lst = list(map(int, stdin.readline().strip().split()))
    i = 0
    while i < len(lst) and lst[i] != -1:
        new_node = ListNode(lst[i])
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
    t = int(stdin.readline().strip())
    while t > 0:
        head = take_input()
        position = int(stdin.readline().strip())
        head = delete_node(head=head, position=position)
        print_linked_list(head=head)
        t -= 1


if __name__ == '__main__':
    main()

# 1
# 3 4 5 2 6 1 9 -1
# 3