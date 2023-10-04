from sys import stdin, setrecursionlimit

'''Time complexity: O(n)
   Space complexity: O(1)'''


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def find_node(head, n):
    current = head
    position = 0
    while current:
        if current.data == n:
            return position
        position += 1
        current = current.next
    return -1


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
        h = take_input()
        n = int(stdin.readline().strip())
        print(find_node(head=h, n=n))
        t -= 1


if __name__ == '__main__':
    main()

# 1
# 18 21 9 4 10 15 -1
# 4