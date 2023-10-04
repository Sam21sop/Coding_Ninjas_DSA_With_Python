from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10**6)

def reverse_queue(input_queue):
    if input_queue.empty():
        return
    front_element = input_queue.get()       #dequeue element from the queue
    reverse_queue(input_queue)              #recursive call to get remaining elem
    input_queue.put(front_element)


def take_input():
    n = int(stdin.readline().strip())
    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))
    for i in range(n):
        qu.put(values[i])
    return qu


def display(queue):
    while not queue.empty():
        print(queue.get(), end=' ')
    print()


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        q = take_input()
        reverse_queue(q)
        display(q)
        t -= 1

if __name__ == "__main__":
    main()


# 1
# 6
# 1 2 3 4 5 10