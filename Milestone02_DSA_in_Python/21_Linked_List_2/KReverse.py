from sys import stdin, setrecursionlimit

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


def k_reverse(head, k):
    if k == 0 or k == 1 or head is None or head.next is None:
        return head
    current = head
    previous = None
    next_node = None
    for _ in range(k):
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    if next_node is not None:
        head.next = k_reverse(next_node, k)
    return previous


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
    t = int(stdin.readline().strip())
    while t > 0:
        head = take_input()
        k = int(stdin.readline().strip())
        new_head = k_reverse(head, k)
        display_linked_list(new_head)
        t -= 1


if __name__ == '__main__':
    main()

# 1
# 1 2 3 4 5 6 7 8 9 10 -1
# 4