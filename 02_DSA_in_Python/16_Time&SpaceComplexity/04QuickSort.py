def partition(array, low,  high):
    pivot = array[high]
    i = low-1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)


def main():
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(*arr)


if __name__ == "__main__":
    main()