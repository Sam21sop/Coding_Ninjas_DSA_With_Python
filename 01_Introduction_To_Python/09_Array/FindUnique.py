from sys import stdin

def findUnique(arr, n):
    unique_count = 1
    for i in range(n):
        if arr.count(arr[i]) > unique_count:
            unique_count = arr.count(arr[i])
            res = arr[i]
    return res


def findUnique(arr, n):
    unique_count = 1
    for i in range(n):
        if arr.count(arr[i]) > unique_count:
            unique_count = arr.count(arr[i])
            res = arr[i]
    return res


def take_input():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


if __name__ == '__main__':
    t = int(stdin.readline().rstrip())
    while t > 0:
        arr, n = take_input()
        print(findUnique(arr, n))
        t -= 1
