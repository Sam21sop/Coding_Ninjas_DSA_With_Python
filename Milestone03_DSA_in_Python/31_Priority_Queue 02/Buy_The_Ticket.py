from sys import stdin, setrecursionlimit
import heapq as heap


class LinkedListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0


    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return
    

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    

    def getSize(self):
        return self.size
    

    def isEmpty(self):
        if self.head is None:
            return True
        return False


    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    

def buy_ticket(lst, size, k):
    q = Queue()
    max_heap = []                   #max Priority queue
    heap.heapify(max_heap)
    for elem in lst:
        q.enqueue(elem)
        heap.heappush(max_heap, -1 * elem)          # add k element in max heap by negate element
    count = 0
    while len(max_heap) != 0:
        if q.peek() == -1 * max_heap[0]:
            if k == 0:
                return count + 1
            else:
                count += 1
                q.dequeue()
                heap.heappop(max_heap)
                k -= 1
        else:
            q.enqueue(q.peek())
            q.dequeue()
            if k == 0:
                k = q.getSize() - 1 
            else:
                k -= 1
    return count


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return n, list(), int(stdin.readline().strip())
    return n, list(map(int, stdin.readline().strip().split())), int(stdin.readline().strip())


def main():
    arr_size, lst, k = take_input()
    ans = buy_ticket(lst, arr_size, k)
    print(ans)


if __name__ == '__main__':
    main()