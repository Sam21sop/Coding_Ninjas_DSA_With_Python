from sys import stdin

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(' ')))
    return arr


if __name__ == '__main__':
    arr = takeInput()
    target = int(stdin.readline().strip())
    result = linearSearch(arr, target)
    print(f'Element found at index: {result}.')
