class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def updated_linked_list(head):
    pass




def take_input():
    head = None
    tail = None
    lst = list(map(int, input().split()))
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
    pass


if __name__ == "__main__":
    main()