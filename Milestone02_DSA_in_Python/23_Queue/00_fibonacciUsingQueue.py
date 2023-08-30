from QueueUsingArray import Queue


def fun(n):
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    for i in range(n+1):
        a = q.dequeue()
        b = q.dequeue()
        q.enqueue(b)
        q.enqueue(a+b)
        print(a)

fun(10)