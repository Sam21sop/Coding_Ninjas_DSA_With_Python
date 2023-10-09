from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def selectionSort(arr, n):
    '''Selection Sort Algorithm.'''
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def takeInput():
    '''Helper function for taking user input.'''
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(' ')))
    return arr, n


if __name__ == '__main__':
    arr, n = takeInput()
    result = selectionSort(arr, n)
    print(*result)