from sys import stdin

def pushZerosAtEnd(arr, n):
    k = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(' ')))
    return arr, n


if __name__ == '__main__':
    array, n = take_input()
    pushZerosAtEnd(array, n)
    print(*array)
