from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)


def is_sorted_better(array, start_index):
    size = len(array)
    if start_index == size-1:
        return True
    if array[start_index] > array[start_index+1]:
        return False
    return is_sorted_better(array, start_index+1)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array


def main():
    arr = take_input()
    result = is_sorted_better(arr, 0)
    print(result)


if __name__ == '__main__':
    main()