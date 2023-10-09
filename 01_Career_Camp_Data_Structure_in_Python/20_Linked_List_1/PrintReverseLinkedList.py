from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def print_reverse(head):
    if head is None:
        return
    print_reverse(head.next)
    print(head.data, end=' ')


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
        print_reverse(head=head)
        t -= 1


if __name__ == '__main__':
    main()

# 1
# 1 2 3 4 5 -1