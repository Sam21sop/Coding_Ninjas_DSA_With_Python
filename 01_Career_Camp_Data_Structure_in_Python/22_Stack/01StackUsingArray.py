class Stack:
    def __init__(self) -> None:
        self.stack = []


    def size(self):
        return len(self.stack)


    def is_empty(self):
        return self.size() == 0
    

    def push(self, element):
        self.stack.append(element)


    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Popping from empty stack")


    def top(self):
        if self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError(-1)
        
    def show(self):
        for i in self.stack:
            print(i, end=' ')
        print('<--Top ele')
        


def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.show()
    stack.pop()
    stack.show()
    print(stack.size())
    print(stack.is_empty())


if __name__ == '__main__':
    main()