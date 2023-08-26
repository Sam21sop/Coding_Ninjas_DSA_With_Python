'''
Time Complexity: O(1)
Space Complexity: O(n)
where n is the number of operation
'''
from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    '''Stack class: Using linked list'''
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__head is None
    
    def push(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__size += 1
    
    def pop(self):
        if self.__head is None:
            return -1
        ans = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return ans

    def top(self):
        if self.__head is None:
            return -1
        return self.__head.data
    


def main():
    q = int(stdin.readline().strip())
    stack = Stack()
    while q > 0:
        user_input = stdin.readline().strip().split()
        choice = int(user_input[0])
        if choice == 1:
            data = int(user_input[1])
            stack.push(data)

        elif choice == 2:
            print(stack.pop())

        elif choice == 3:
            print(stack.top())

        elif choice == 4:
            print(stack.get_size())

        else:
            if stack.is_empty():
                print("true")
            else:
                print("false")

        q -= 1

if __name__ == '__main__':
    main()
    
# 6
# 1 13
# 1 47
# 4
# 5
# 2
# 3