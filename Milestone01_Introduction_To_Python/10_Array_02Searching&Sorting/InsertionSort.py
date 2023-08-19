from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def recursive_insertion_sort(array, size):
    #if size of array 1 or 0 is sorted
    if size <= 1:
        return
    
    #recursively sort the first (size-1) items
    recursive_insertion_sort(array, size-1)

    #insert Nth item in the sorted array
    key = array[size-1]
    i = size - 2
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    recursive_insertion_sort(arr, n)
    print(*arr)
