from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def swapNodes(head, i, j) :
	#Your code goes here
    if head is None or i == j:
        return head
    prev1 = None
    prev2 = None
    node1 = head
    node2 = head
    count = 0
    while count < i and node1:
        prev1 = node1
        node1 = node1.next
        count += 1
    count = 0
    while count < j and node2:
        prev2 = node2
        node2 = node2.next
        count += 1
    if node1 is None and node2 is None:
        return head
    if prev1:
        prev1.next = node2
    else:
        head = node2
    if prev2:
        prev2.next = node1
    else:
        head = node1
    node1.next, node2.next = node2.next, node1.next
    return head


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
    i_j = stdin.readline().strip().split(" ")
    i = int(i_j[0])
    j = int(i_j[1])
    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)
    t -= 1