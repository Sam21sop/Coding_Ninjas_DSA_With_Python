from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def binarySearch(arr, target):
    '''Binary search algorithm'''
    n = len(arr)
    start = 0
    end = n - 1
    middle = start
    for i in range(start, end+1):
        middle = start + (end-start) // 2
        if arr[middle] > target:
            end = middle - 1
        elif arr[middle] < target:
            start = middle + 1
        else:
            return middle
    return -1

def takeinput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(' ')))
    return arr, n 

            
if __name__ == '__main__':
    arr, n = takeinput()
    target = int(stdin.readline().strip())
    result = binarySearch(arr, target)
    print(f'Element found at index: {result}.')
