from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def is_sorted(array):
    if len(array) == 1:
        return True
    if array[0] > array[1]:
        return False
    small_array = [0] * (len(array)-1)
    for i in range(1, len(array)):
        small_array[i-1] = array[i]
    is_small_array_sorted = is_sorted(small_array)
    return is_small_array_sorted


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array


def main():
    arr = take_input()
    result = is_sorted(arr)
    print(result)

if __name__ == '__main__':
    main()