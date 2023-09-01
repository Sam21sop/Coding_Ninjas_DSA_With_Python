class QueueUsingStack:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    

    def isEmpty(self):
        return not self.stack1 and not self.stack2
    
    def size(self):
        return len(self.stack1) + len(self.stack2)
    

def main():
    q = QueueUsingStack()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Dequeued element:", q.dequeue())  
    print("Queue size:", q.size()) 
    print("Is queue empty?", q.isEmpty())


if __name__ == "__main__":
    main()