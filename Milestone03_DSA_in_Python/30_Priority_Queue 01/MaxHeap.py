class MaxHeap:
    def __init__(self) -> None:
        self.heap = []


    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)


    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_value
    

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index-1)// 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break


    def _heapify_down(self, index):
        left_child_index = (2*index) + 1
        right_child_index = (2*index) + 2
        largest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    
    
    def display(self):
        while self.heap:
            print(self.heap.pop(), end=' ')
        print()


def main():
    pq = MaxHeap()
    pq.push(3)
    pq.push(1)
    pq.push(2)
    pq.display()


if __name__ == '__main__':
    main()