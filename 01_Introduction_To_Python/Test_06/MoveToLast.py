from math import *
from collections import *
from sys import *
from os import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


def constructLinkedList(nums):
    head = Node(nums[0])
    current = head
    for n in nums[1:]:
        if n == -1:
            break
        new_node = Node(n)
        current.next = new_node
        current = new_node
    return head


def moveKeyToEnd(head, key):
    #dummy node for before and after the key
    after_key = Node(None)
    after_key_tail = after_key

    before_key = Node(None)
    before_key_tail = before_key

    current = head
    while current:
        if current.data == key:
            after_key_tail.next = current
            after_key_tail = after_key_tail.next
        else:
            before_key_tail.next = current
            before_key_tail = before_key_tail.next
        current = current.next
    
    #connect the end
    before_key_tail.next = after_key.next
    after_key_tail.next = None
    head = before_key.next
    return head


def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()



#read teh input form the stdin
nums = list(map(int, stdin.readline().strip().split()))
key = int(stdin.readline().strip())

head = constructLinkedList(nums)
updated_head = moveKeyToEnd(head, key)
printLinkedList(updated_head)