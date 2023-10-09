import sys
# from decimal import Decimal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def constructLinkedList(nums):
    '''Function form a linked list using array list'''
    head = Node(nums[0])
    current = head
    for num in nums[1:]:
        if num == -1:
            break
        new_node = Node(num)
        current.next = new_node
        current = new_node
    return head

def calculateNumber(head):
    '''Function return the number.'''
    number = 0
    while head:
        number = number * 10 + head.data
        head = head.next
    return number

def multiplyLinkedLists(list1, list2):
    '''Function return the product of number.'''
    num1 = calculateNumber(list1)
    num2 = calculateNumber(list2)
    product = num1 * num2
    return product



# Read the input lists
list1 = list(map(int, sys.stdin.readline().strip().split()))
list2 = list(map(int, sys.stdin.readline().strip().split()))


# Construct linked lists
linked_list1 = constructLinkedList(list1)
linked_list2 = constructLinkedList(list2)


# Calculate the product of the two numbers
product = multiplyLinkedLists(linked_list1, linked_list2)

# Print the product
for i in str(product):
    print(i, end=' ')