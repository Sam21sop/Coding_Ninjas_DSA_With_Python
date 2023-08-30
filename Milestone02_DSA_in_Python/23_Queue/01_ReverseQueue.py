from QueueUsingArray import Queue

def fun(q):
    if not q.is_empty():
        i = q.dequeue()
        fun(q)
        q.enqueue(i)


def main():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("Original Queue:", *q.data)
    fun(q)
    print("Queue after applying f:", *q.data)

if __name__ == '__main__':
    main()
