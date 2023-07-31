from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)


def lastIndex(array:list[int], number:int):
    arr_size = len(array)
    if arr_size <= 0:
        return -1
    result = lastIndex(array[1:], number)
    if result == -1:
        if number == array[0]:
            return 0
        else:
            return -1
    return result + 1


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array


def main():
    arr = take_input()
    num = int(stdin.readline().strip())
    result = lastIndex(arr, num)
    print(result)


if __name__ == '__main__':
    main()