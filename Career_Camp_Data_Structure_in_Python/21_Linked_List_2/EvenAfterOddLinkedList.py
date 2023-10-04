from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def even_after_odd(head):
    if head is None:
        return head
    #create a dummy node
    odd_head = Node(0)
    even_head = Node(0)
    #point tail to dummy node
    odd_tail = odd_head
    even_tail = even_head
    current = head
    while current:
        if current.data % 2 == 1:
            odd_tail.next = current
            odd_tail = odd_tail.next
        else:
            even_tail.next = current
            even_tail = even_tail.next
        current = current.next
    odd_tail.next = even_head.next
    even_tail.next = None
    return odd_head.next


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

def show_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

def main():
    t = int(stdin.readline().strip())
    while t > 0:
        head = take_input()
        new_head = even_after_odd(head=head)
        show_linked_list(new_head)
        t -= 1

if __name__ == '__main__':
    main()