class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

n1 = Node(20)
head.next = n1

n2 = Node(30)
n1.next = n2

n3 = Node(40)
n2.next = n3

current = head

while current != None:
    print(current.data, end='-->') 
    temp = current.next
    current = temp
print()