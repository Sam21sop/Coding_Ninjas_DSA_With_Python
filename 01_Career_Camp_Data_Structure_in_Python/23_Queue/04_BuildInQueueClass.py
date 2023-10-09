from queue import Queue
from collections import deque

q1 = deque([10, 20, 30, 40, 50])
print(q1)
print(q1.pop())
print(q1)
q1.append(50)
print(q1)
q1.appendleft(60)
print(q1)
q1.popleft()
print(q1)


q2 = Queue(5)
print(q2.empty())
q2.put(10)
q2.put(20)
q2.put(30)
q2.put(40)
q2.put(50)
print(q2.empty())
print(q2)