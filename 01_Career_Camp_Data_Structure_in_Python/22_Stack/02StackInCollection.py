from collections import deque

#crating stack
stack = deque([10, 20 , 30, 40, 50])

#print stack
print(stack)

#add element to the stack
stack.append(99)
print(stack)

#pop element
print(stack.pop())
print(stack)

#size
print(len(stack))

#reverse stack
stack.reverse()
print(stack)
stack.rotate(2)
print(stack)