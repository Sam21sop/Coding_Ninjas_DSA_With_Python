from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def bubleSort(arr, size):
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr


def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(' ')))
    return arr, n


if __name__ == '__main__':
    arr, n = takeInput()
    result = bubleSort(arr, n)
    # print(*result)
