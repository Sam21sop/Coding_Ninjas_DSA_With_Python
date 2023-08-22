from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def get_mid(head):
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_linked_list(head1, head2):
    dummy = Node(0)
    current = dummy
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
        if head1:
            current.next = head1
        if head2:
            current.next = head2
    return dummy.next


def merge_sort(head) :
    '''Function return sorted linked list'''
    if head is None or head.next is None:
        return head
    #find the middle linked list
    middle = get_mid(head)
    middle_next = middle.next
    middle.next = None
    #recursively sort first and second half
    left_half = merge_sort(head)
    right_half = merge_sort(middle_next)
    #merge the sorted halfs
    sorted_linked_list = merge_linked_list(left_half, right_half)
    return sorted_linked_list


def takeInput() :
    head = None
    tail = None
    datas = list(map(int, stdin.readline().rstrip().split(" ")))
    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)
        if head is None :
            head = newNode
            tail = newNode
        else :
            tail.next = newNode
            tail = newNode
        i += 1
    return head

def show_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

    
def main():
    t = int(stdin.readline().rstrip())
    while t > 0 :
        head = takeInput()
        newHead = merge_sort(head)
        show_linked_list(newHead)
        t -= 1


if __name__ == '__main__':
    main()