from sys import stdin

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    '''Queue class using linked list'''
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0

    
    def getSize(self):
        return self.__size
    

    def isEmpty(self):
        return self.__size == 0
    

    def enqueue(self, element):
        self.__size += 1
        new_node = Node(element)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node


    def dequeue(self):
        if self.isEmpty():
            return -1
        ans = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return ans

    
    def front(self):
        if self.__head is None:
            return -1
        return self.__head.data
    
    def display(self):
        while self.__head is None:
            print(self.__head.data)
            self.__head = self.__head.next
        print()
    

def main():
    t = int(stdin.readline().strip())
    q = Queue()
    while t > 0:
        lst = stdin.readline().strip().split()
        choice = int(lst[0])
        if choice == 1:
            data = int(lst[1])
            q.enqueue(data)
        elif choice == 2:
            print(q.dequeue())
        elif choice == 3:
            print(q.front())
        elif choice == 4:
            print(q.getSize())
        else:
            if q.isEmpty():
                print('true')
            else:
                print('false')
        t -= 1


if __name__ == "__main__":
    main()