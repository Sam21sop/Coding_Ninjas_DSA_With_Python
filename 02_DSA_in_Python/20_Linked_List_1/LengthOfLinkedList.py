class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    if not head:
        return 
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    return count

def build_linked_list(array):
    if not array:
        return 
    head = Node(array[0])
    current = head
    for value in array[1:]:
        new_node = Node(value)
        #linked together previous and current node
        current.next = new_node
        #current refering to new_node
        current = new_node
    return head

def main():
    lst = list(map(int, input().split()))
    head = build_linked_list(lst)
    size = length(head)
    print(size)


if __name__ == '__main__':
    main()