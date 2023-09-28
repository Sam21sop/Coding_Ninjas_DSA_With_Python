'''
Time Complexity: O(logn)  ==> where n is input array size
Space Complexity: O(1)
'''

def down_heapify(arr, size, index):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        down_heapify(arr, size,  largest)


def heapSort(arr):
    size = len(arr)
    #build a Max heap
    for index in range(size//2 - 1, -1, -1):
        down_heapify(arr, size, index)

    #extract element one by one from heap
    for size in range(size-1, 0, -1):
        arr[size], arr[0] = arr[0], arr[size]
        down_heapify(arr, size, 0)


def main():
    n = input()
    arr = [int(i) for i in input().split()]
    heapSort(arr)
    for i in arr[::-1]:
        print(i, end=' ')


if __name__ == '__main__':
    main()