def array_partition(array, start, end):
    pivot_element = array[start]
    small_num_count = 0
    for i in range(start+1, end+1):
        if array[i] < pivot_element:
            small_num_count += 1
    array[small_num_count + start], array[start] = array[start], array[small_num_count]
    i = start
    j = end
    while i < j:
        if array[i] < pivot_element:
            i += 1
        elif array[j] >= pivot_element:
            j += 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return start + small_num_count


def quickSort(array, start, end):
    if start > end:
        return -1
    pivot_index = array_partition(array, start, end)
    quickSort(array, start, pivot_index-1)
    quickSort(array, pivot_index+1, end)

