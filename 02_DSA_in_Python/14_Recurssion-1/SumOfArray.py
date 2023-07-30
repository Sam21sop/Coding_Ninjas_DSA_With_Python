from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def array_sum(array, size):
    
    if size <= 0:
        return 0
    return array[size-1] + array_sum(array, size-1)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def main():
    arr, n = take_input()
    result = array_sum(arr, n)
    print(result)


if __name__ == '__main__':
    main()