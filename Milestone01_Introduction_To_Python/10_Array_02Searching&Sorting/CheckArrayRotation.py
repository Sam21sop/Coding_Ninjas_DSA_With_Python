from sys import stdin


def array_rotate_check(array:list[int], size:int):
    for i in range(size-1):
        if array[i] > array[i+1]:
            return [i+1]
    return 0


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        print(array_rotate_check(arr, n))
        t -= 1

        