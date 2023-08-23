from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def find_node_rec(head, data, index=0):
    if head is None:
        return head
    if head.data == data:
        return index
    return find_node_rec(head.next, data, index+1)

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
        key = int(stdin.readline().strip())
        print(find_node_rec(head=head, data=key))
        t -= 1


if __name__ == '__main__':
    main()


# 1
# 10 20010 30 400 600 -1
# 20010