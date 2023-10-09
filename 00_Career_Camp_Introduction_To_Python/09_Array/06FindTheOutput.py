def mul(arr):
    for i in range(0, 5):
        arr[i] *= i


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    mul(arr)
    for i in range(0, 5):
        print(arr[i], end=' ')