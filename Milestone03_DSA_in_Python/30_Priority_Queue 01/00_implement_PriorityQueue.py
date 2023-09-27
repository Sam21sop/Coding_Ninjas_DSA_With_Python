class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    
    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError('Heap is empty')
        return self.heap[0]
    

    def size(self):
        return len(self.heap)
    

    def is_empty(self):
        return len(self.heap) == 0
    

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError('heap is empty')
        if len(self.heap) == 1:
            return self.heap.pop()
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_value
    

    def __heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.__heapify_down(smallest)


    def display(self):
        for item in self.heap:
            print(item, end=' ')
        print()



def main():
    pq = MinHeap()
    pq.push(3)
    pq.push(1)
    pq.push(2)
    pq.display()
         

if __name__ == '__main__':
    main()