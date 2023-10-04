from sys import stdin, setrecursionlimit

'''
Time complexity: O(n),  Where n is size of linked list
Space Complexity: O(1)
'''

class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def insert_node(head, position, data):
    current_pos = 0
    new_node = ListNode(data)
    if position == 0:
        new_node.next = head
        head = new_node
        return head
    temp = head
    while temp is not None and current_pos < (position-1):
        temp = temp.next
        current_pos += 1
    if temp is None:
        return head
    new_node.next = temp.next
    temp.next = new_node
    return head


#taking input using fast I/O
def take_input():
    head = None
    tail = None
    data_list = list(map(int, stdin.readline().strip().split()))
    i = 0
    while i < len(data_list) and data_list[i] != -1:
        new_node = ListNode(data_list[i])
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
            i += 1
        i += 1
    return head


#display linked list
def display_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" --> ")
        current = current.next
    print()


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        head = take_input()
        positino_data = stdin.readline().strip().split()
        position = int(positino_data[0])
        data = int(positino_data[1])
        head = insert_node(head=head, position=position, data=data)
        display_linked_list(head=head)
        t -= 1


if __name__ == '__main__':
    main()

# 1
# 3 4 5 2 6 1 9 -1
# 3 100