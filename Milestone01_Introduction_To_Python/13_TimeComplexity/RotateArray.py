from sys import stdin

def swap_element(array, start, end):
    array[start], array[end] = array[end], array[start]


def reverse(array, start, end):
    while start < end:
        swap_element(array, start, end)
        start += 1
        end -= 1


def rotate(array, size, d):
    if size == 0:
        return
    if d >= size and size != 0:
        d %= size
    reverse(array, 0, size-1)
    reverse(array, 0, size-d-1)
    reverse(array, size-d, size-1)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def print_array(array, n):
    for i in range(n):
        print(array[i], end=' ')
    print()


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        rotation_by_d = int(stdin.readline().strip())
        rotate(arr, n, rotation_by_d)
        print_array(arr, n)
        t -= 1


if __name__ == '__main__':
    main()