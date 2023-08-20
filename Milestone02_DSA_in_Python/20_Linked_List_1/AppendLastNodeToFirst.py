from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def append_last_node_first(head, n):
    if n == 0 or head is None:
        return head
    fast = head
    slow = head
    intitial_head = head
    for i in range(n):
        fast = fast.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    temp = slow.next
    slow.next = None
    fast.next = intitial_head
    head = temp
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
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        h = take_input()
        k_node = int(stdin.readline().strip())
        head = append_last_node_first(head=h, n=k_node)
        display_linked_list(head=head)
        t -= 1


if __name__ == '__main__':
    main()

# 1
# 10 6 77 90 61 67 100 -1
# 4