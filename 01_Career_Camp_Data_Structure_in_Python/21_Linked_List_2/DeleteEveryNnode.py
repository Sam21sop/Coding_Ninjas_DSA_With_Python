from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def skipMdeleteN(head, M, N) :
    # If M is 0, return the original linked list
    if M == 0:
        return None
    # If N is 0, delete all the nodes after every M nodes
    if N == 0:
        return head
    # If the list is empty or contains only one element
    if not head or not head.next:
        return head
    current = head
    prev = None
    while current:
        # Traverse M nodes
        for _ in range(M):
            if not current:
                return head
            prev = current
            current = current.next
        # Delete N nodes
        for _ in range(N):
            if not current:
                break
            current = current.next
        # Update the next pointer of the previous node
        prev.next = current
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
    m_n = stdin.readline().strip().split(" ")
    m = int(m_n[0])
    n = int(m_n[1])
    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)
    t -= 1

# 1
# 10 22 10 26 11 7 -1
# 0 3