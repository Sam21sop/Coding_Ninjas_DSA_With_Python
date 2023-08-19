from sys import stdin, setrecursionlimit

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_linked_list_from_input():
    input_list = list(map(int, input().split()))
    if not input_list:
        return None
    head = ListNode(input_list[0])
    current = head
    for data in input_list[1:]:
        new_node = ListNode(data)
        current.next = new_node
        current = new_node
    return head


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=' --> ')
        current = current.next
    print("None")


def main():
    Linked_list_head = build_linked_list_from_input()
    print("Linked List: ", display_linked_list(Linked_list_head))

if __name__ == '__main__':
    main()