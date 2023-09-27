class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []


    def isEmpty(self):
        pass


    def getSize(self):
        pass


    def getMax(self):
        pass


    def parent(self, index):
        pass


    def __heapify_up(self, index):
        pass


    def insert(self):
        pass


    def left_child(self):
        pass


    def right_child(self):
        pass


    def __heapify_down(self, index):
        pass

    
    def remove_max(self):
        pass


def main():
    pq = PriorityQueue()
    current_input = [int(i) for i in input().strip().split()]
    choice = current_input[0]
    i = 1
    while choice != -1:
        if choice  == 1:
            element = current_input[i]
            i += 1
            pq.insert(element, element)
        elif choice == 2:
            print(pq.getMax())
        elif choice == 3:
            print(pq.removeMax())
        elif choice == 4:
            print(pq.getSize())
        elif choice == 5:
            if pq.isEmpty():
                print('true')
            else:
                print('false')
            break
        else:
            pass
        choice = current_input[i]
        i+=1


if __name__ == '__main__':
    main()