from sys import stdin


def swap_element(array:list[int], start:int, end:int):
    array[start], array[end] = array[end], array[start]


def reverse(array:list[int], start:int, end:int):
    while start < end:
        swap_element(array, start, end)
        start += 1
        end -= 1


def rotate(arr:list[int], n:int, d:int):
    if n == 0:
        return
    if d >= n and n != 0:
        d = d % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, n-d-1)
    reverse(arr, n-d, n-1)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split(' ')))
    return array, n


def print_list(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        d = int(stdin.readline().strip())
        rotate(arr, n, d)
        print_list(arr, n)
        t -= 1
