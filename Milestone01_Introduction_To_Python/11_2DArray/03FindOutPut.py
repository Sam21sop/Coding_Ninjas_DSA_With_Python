def fun(arr):
    s = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            s += arr[i][j]
    return s


if __name__ == '__main__':
    arr = [[0, 1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [5, 6, 7, 8, 9]]
    print(fun(arr))