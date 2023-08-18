class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def increment_every_node_value(head):
    if head is None:
        return
    current = head
    while current:
        current.data += 1
        print(current.data, end='-->')
        temp = current.next
        current = temp
    

def build_linked_list(array):
    if not array:
        return
    head = Node(array[0])
    current = head
    for data in array[1:]:
        new_node = Node(data)
        current.next = new_node
        current = new_node
    return head


def main():
    lst = list(map(int, input().split()))
    head = build_linked_list(lst)
    increment_every_node_value(head)


if __name__ == '__main__':
    main()