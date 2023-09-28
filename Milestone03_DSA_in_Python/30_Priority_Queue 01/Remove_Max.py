class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []


    def isEmpty(self):
        return len(self.heap) ==  0


    def getSize(self):
        return len(self.heap)


    def getMax(self):
        if self.isEmpty():
            return
        return self.heap[0][0]


    def parent(self, index):
        return  (index - 1) // 2


    def __heapify_up(self, index):
        while index > 0 and self.heap[index][1] > self.heap[self.parent(index)][1]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)


    def insert(self, element, priority):
        node = (element, priority)
        self.heap.append(node)
        self.__heapify_up(len(self.heap)-1)


    def left_child(self, index):
        return 2 * index + 1


    def right_child(self, index):
        return 2 * index + 2


    def __heapify_down(self, index):
        max_index = index
        left = self.left_child(index)
        right = self.right_child(index)
        if left < len(self.heap) and self.heap[left][1] > self.heap[max_index][1]:
            max_index = left
        if right < len(self.heap) and self.heap[right][1] > self.heap[max_index][1]:
            max_index = right
        if max_index != index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self.__heapify_down(max_index)

        
    def remove_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[0]

        max_value = self.heap[0][0]
        self.heap[0] = self.heap.pop()
        self.__heapify_down(0)
        return max_value


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
            print(pq.remove_max())
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