from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def kReverse(head, k):
    if head is None:
        return
    prev = None
    curr = head
    next_node = None
    count = 0
    while count < k and curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
    if next_node is not None:
        head.next = kReverse(next_node, k)
    return prev


def build(arr, num_of_node):
    if num_of_node == 0:
        head = None
    else:
        head = Node(arr[0])
        curr = head
        for value in arr[1:]:
            curr.next = Node(value)
            curr = curr.next
    return head


def display(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()


def main():
    num_of_node = int(input())
    elements_arr = list(map(int, stdin.readline().strip().split()))
    k = int(input())
    head = build(elements_arr, num_of_node)
    new_head = kReverse(head, k)
    display(new_head)

if __name__ == '__main__':
    main()