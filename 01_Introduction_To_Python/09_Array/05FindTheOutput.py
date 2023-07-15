def arr_sum(arr):
    arr_s = []
    for i in range(0, 5):
        arr_s.append(arr[i])
    return sum(arr_s)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    result = arr_sum(arr)
    print(result)
