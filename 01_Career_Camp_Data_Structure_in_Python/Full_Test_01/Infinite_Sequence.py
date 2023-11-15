def serach(array, x:int, index:int):
    for i in range(index-2, -1, -1):
        if array[i] == x:
            return i
    return -1


def main():
    a = [0] * 128
    a[0] = 0
    for i in range(1, 128):
        index = serach(a, a[i-1], i)
        if index == -1:
            a[i] = 0
        else:
            a[i] = i - index - 1
    n = int(input())
    count = 0
    for i in range(n):
        if a[i] == a[n-1]:
            count += 1
    print(count)


if __name__ == '__main__':
    main()