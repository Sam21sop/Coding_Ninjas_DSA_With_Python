from sys import stdin
import queue


def reverseKElements(inputQueue, k):
    if inputQueue.qsize() > k:
        k = k % inputQueue.qsize()
    if k == 0 or k == 1:
        return inputQueue
    reverseQueue(inputQueue, k)
    for i in range(inputQueue.qsize()-k):
        inputQueue.put(inputQueue.get())
    return inputQueue


def reverseQueue(inputQueue, k):
    if inputQueue.qsize() == 0 or inputQueue.qsize() == 1 or k == 0:
        return
    temp = inputQueue.get()
    reverseQueue(inputQueue, k-1)
    inputQueue.put(temp)


def isEmpty(stack):
    return len(stack) == 0


def top(stack):
    return stack[len(stack)-1]


def take_input():
    n_k = list(map(int, stdin.readline().strip().split()))
    n = n_k[0]
    k = n_k[1]
    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))
    for i in range(n):
        qu.put(values[i])
    return k, qu


def display(queue):
    while not queue.empty():
        print(queue.get(), end=' ')
    print()


def main():
    k, q = take_input()
    qu = reverseKElements(q, k)
    display(qu)


if __name__ == '__main__':
    main()

# 5 3
# 1 2 3 4 5