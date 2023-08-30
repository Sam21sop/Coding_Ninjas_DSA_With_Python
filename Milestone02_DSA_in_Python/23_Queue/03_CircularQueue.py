class CircularQueue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1


    def is_empty(self):
        return self.front == -1
    

    def is_full(self):
        return (self.rear+1) % self.capacity == self.front
    

    def enqueue(self, element):
        if self.is_full():
            print("Queue is Full")
            return None
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] = element


    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        removed_element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_element
    

    def front_element(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        return self.queue[self.front]
    

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        index = self.front
        while True:
            print(self.queue[index], end=' ')
            if index == self.rear:
                break
            index = (index+1) % self.capacity
        print()


def main():
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)

    print("Queue elements:")
    cq.display()

    print("Dequeue:", cq.dequeue())
    print("Dequeue:", cq.dequeue())

    cq.enqueue(5)
    cq.enqueue(6)

    print("Queue elements:")
    cq.display()

    print("Front element:", cq.front_element())


if __name__ == '__main__':
    main()