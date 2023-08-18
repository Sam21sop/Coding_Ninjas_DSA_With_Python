class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def ith_element(head, i):
    position = 0
    current = head
    while current and position < i:
        current = current.next
        position += 1
    if current:
        print(current.data)



def take_input():
    head = None
    tail = None
    data_lst = list(map(int, input().split()))
    i = 0
    while i < len(data_lst) and data_lst[i] != -1:
        new_node = Node(data_lst[i])
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
        i += 1
    return head


def main():
    t = int(input())
    while t > 0:
        head = take_input()
        i = int(input())
        ith_element(head, i)
        t -= 1


if __name__ == "__main__":
    main()