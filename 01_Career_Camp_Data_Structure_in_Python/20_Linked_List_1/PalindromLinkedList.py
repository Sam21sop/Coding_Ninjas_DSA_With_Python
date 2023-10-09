from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def is_palindrom(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    #reverse Second Half
    previous = None
    current = slow
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    #check both are equal or not
    first_half = head
    second_half = previous
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True


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


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        head = take_input()
        if is_palindrom(head=head):
            print('true')
        else:
            print('false')
        t -= 1

if __name__ == '__main__':
    main()


# 1
# 12 3 5 3 2 -1
