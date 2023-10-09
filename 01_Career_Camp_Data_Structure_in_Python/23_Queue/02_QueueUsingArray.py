class Queue:
    def __init__(self) -> None:
        self.data = []
        self.front = -1
        self.rear = -1

    def get_size(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, element):
        self.data.append(element)
        if self.front == -1:
            self.front = 0
        self.rear = len(self.data)-1


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        removed_element = self.data.pop(self.front)
        if len(self.data) == 0:
            self.front = self.rear = -1
        else:
            self.rear = len(self.data) - 1
        return removed_element


    def front(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        return self.data[self.front]


def main():
    q = Queue()

    q.enqueue(1)   
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("Queue size:", q.get_size())
    
    print("Dequeue:", q.dequeue())
    print("Queue size:", q.get_size())
    
    print("Dequeue:", q.dequeue())
    print("Queue size:", q.get_size())
    
    print("Dequeue:", q.dequeue())
    print("Queue size:", q.get_size())
    print("Is the queue empty?", q.is_empty())



if __name__ == '__main__':
    main()
