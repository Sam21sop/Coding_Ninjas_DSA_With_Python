from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def getMiddle(head):
    '''Function return the middle node. '''
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1, head2):
    '''Function return the merged link list '''
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

    



#Taking Input Using Fast I/O
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


def printLinkedList(head) :
    while head is not None :
        print(head.data, end = " ")
        head = head.next
    print()


#main
t = int(stdin.readline().rstrip())
while t > 0 :
    head = takeInput()
    newHead = mergeSort(head)
    printLinkedList(newHead)
    t -= 1