from sys import stdin, setrecursionlimit

'''Time complexity: O(n)
   Space Complexity: O(1)'''

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def eliminate_duplicates(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
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
    t = int(stdin.readline().strip())
    while t > 0:
        h = take_input()
        head = eliminate_duplicates(head=h)
        display_linked_list(head=head)
        t -= 1

if __name__  == '__main__':
    main()

# 1
# 1 2 3 3 3 3 4 4 4 5 5 7 -1