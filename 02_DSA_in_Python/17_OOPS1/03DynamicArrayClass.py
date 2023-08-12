class DynamicArray:
    def __init__(self) -> None:
        self.__data = []
        self.__size = 0

    def __len__(self):
        self.__size

    def __getitems__(self, index):
        if 0 <= index and index < self.__size:
            return self.__data[index]
        raise IndexError('Index Out of Range')
    
    def append(self, value):
        self.__data.append(value)
        self.__size += 1
    
    def remove(self, index):
        if 0 <= index and index < self.__size:
            del self.__data[index]
            self.__size -= 1
        else:
            raise IndexError('Index Out of Range')
        
    def display(self):
        print(self.__data)


def main():
    # Creating a dynamic array instance
    dyn_array = DynamicArray()

    # Appending values
    dyn_array.append(5)
    dyn_array.append(10)
    dyn_array.append(15)

    # Displaying array
    dyn_array.display()  # Output: [5, 10, 15]

    # Removing element at index 1
    dyn_array.remove(1)

    # Displaying updated array
    dyn_array.display()  # Output: [5, 15]


if __name__ == '__main__':
    main()