from sys import stdin

def swap_if_greater(array1, array2, ind1, ind2):
    if array1[ind1] > array2[ind2]:
        array1[ind1], array2[ind2] = array2[ind2], array1[ind1]


def merge_two_sorted_array(array1, size_1_arr, array2, size_2_arr):
    length =  size_2_arr + size_1_arr
    gap = (length // 2) + (length % 2)
    while gap > 0:
        left = 0
        right = left + gap
        while right < length:
            if left < size_1_arr and right > size_2_arr:
                swap_if_greater(array1, array2, left, right - size_1_arr)
            elif left >= size_1_arr:
                swap_if_greater(array2, array2, left - size_1_arr, right - size_1_arr) 
            else:
                swap_if_greater(array1, array1, left, right)
            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(' ')))
    return arr, n 


# def print_list(arr, n):
#     for i in range(n):
#         print(arr[i], end=' ')
#     print()


if __name__ == '__main__':
    t = int(stdin.readline().rstrip())
    while t > 0:
        arr1, size1 = take_input()
        arr2, size2 = take_input()
        merge_two_sorted_array(arr1, size1, arr2, size2)
        print(*arr1, *arr2)
        t -= 1
