class PriorityQueueNode:
    def __init__(self, elem, priority) -> None:
        self.elem = elem
        self.priority = priority


class PriorityQueue:
    def __init__(self) -> None:
        self.pq = []

    
    def isEmpty(self):
        return self.getSize() == 0
    

    def getSize(self):
        return len(self.pq)
    

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].elem
    

    def insert(self, elem, priority):
        node = PriorityQueueNode(elem, priority)
        self.pq.append(node)
        self.__heapify_up()


    def __heapify_up(self):
        child_index = self.getSize() - 1
        while child_index > 0:
            parent_index = (child_index - 1) // 2
            if self.pq[parent_index].priority > self.pq[child_index].priority:
                self.pq[parent_index], self.pq[child_index] = self.pq[child_index], self.pq[parent_index]
                child_index = parent_index
            else:
                break


    def remove_min(self):
        if self.isEmpty():
            return
        min_ele = self.pq[0].elem
        last_ele = self.pq.pop()
        if not self.isEmpty():
            self.pq[0] = last_ele
            self.__heapify_down(0)
        return min_ele
    

    def __heapify_down(self, index):
        left_child_index = (2*index) + 1
        right_child_index = (2*index) + 2
        smallest = index

        if left_child_index < self.getSize() and self.pq[left_child_index].priority < self.pq[smallest].priority:
            smallest = left_child_index
        if right_child_index <self.getSize() and self.pq[right_child_index].priority < self.pq[smallest].priority:
            smallest = right_child_index
        if smallest != index:
            self.pq[index], self.pq[smallest] = self.pq[smallest], self.pq[index]
            self.__heapify_down(smallest)


def main():
    pq = PriorityQueue()
    curr_input = [int(i) for i in input().strip().split()]
    choice = curr_input[0]
    i = 1
    while choice != -1:
        if choice == 1:
            element = curr_input[i]
            i += 1
            pq.insert(element, element)
        elif choice == 2:
            print(pq.getMin())
        elif choice == 3:
            print(pq.remove_min())
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
        choice = curr_input[i]
        i += 1


if __name__ == '__main__':
    main()