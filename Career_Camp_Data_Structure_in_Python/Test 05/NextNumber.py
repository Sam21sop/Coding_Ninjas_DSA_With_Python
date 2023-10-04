class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    current = head
    previous = None
    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous


def next_number(head):
    new_head = reverse(head)
    current = new_head
    carry = 1
    previous = None
    while current:
        data = (current.data + carry) % 10
        carry = (current.data + carry) // 10
        current.data = data
        previous = current
        current = current.next
    if carry == 1:
        new_node = Node(carry)
        previous.next = new_node
    head = reverse(new_head)
    return head


def build_linked_list(arr):
    if len(arr) == 0:
        return
    head = Node(arr[0])
    tail = head
    for ele in arr[1:]:
        tail.next = Node(ele)
        tail = tail.next
    return head


def show_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    arr = [int(i) for i in input().split()]
    linked_list = build_linked_list(arr[:-1])
    head = next_number(linked_list)
    show_linked_list(head)


if __name__ == '__main__':
    main()