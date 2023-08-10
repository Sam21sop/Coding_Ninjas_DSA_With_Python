def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def main():
    arr = list(map(int, input().split()))
    sorted_array = merge_sort(arr)
    print(*sorted_array)


if __name__ == '__main__':
    main()