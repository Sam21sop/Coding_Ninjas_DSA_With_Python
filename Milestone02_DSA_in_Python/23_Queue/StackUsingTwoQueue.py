from queue import Queue
from sys import stdin


class Stack :

	def __init__(self):
		self.queue1 = Queue()
		self.queue2 = Queue()


	def getSize(self) :
		return self.queue1.qsize()


	def isEmpty(self) :
		return self.queue1.empty()


	def push(self, data) :
		self.queue1.put(data)


	def pop(self) :
		if self.isEmpty():
			return -1
		while self.queue1.qsize() > 1:
			self.queue2.put(self.queue1.get())
		top_ele = self.queue1.get()
		self.queue1, self.queue2 = self.queue2, self.queue1
		return top_ele



	def top(self) :
		if self.isEmpty():
			return -1
		while self.queue1.qsize() > 1:
			self.queue2.put(self.queue1.get())
		top_ele = self.queue1.get()
		self.queue2.put(top_ele)
		self.queue1, self.queue2 = self.queue2, self.queue1
		return top_ele


#main
q = int(stdin.readline().strip())
stack = Stack()
while q > 0 :
	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])
	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)
	elif choice == 2 :
		print(stack.pop())
	elif choice == 3 :
		print(stack.top())
	elif choice == 4 : 
		print(stack.getSize())
	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")
	q -= 1


# 4
# 5
# 2
# 1 10
# 5