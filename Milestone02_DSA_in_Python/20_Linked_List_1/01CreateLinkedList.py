class Node:
    '''Node class: creating list Node'''
    def __init__(self, data):
        self.data = data 
        self.next = None


def print_linked_list(head):
    '''Print given linked list'''
    current = head
    while current:
        print(current.data, end='-->')
        current = current.next


def build_linked_list(array):
    '''Build Linked list from given array'''
    if not array:
        return None
    head = Node(array[0])
    current = head
    for data in array[1:]:
        new_node = Node(data)
        current.next = new_node
        current = new_node
    return head


def take_input():
    '''Taking input from user'''
    n = int(input())
    if n == 0:
        return list(), 0
    lst = list(map(int, input().split()))
    return lst


def main():
    '''This a main function'''
    lst = take_input()
    head = build_linked_list(lst)
    print_linked_list(head)


if __name__ == '__main__':
    main()