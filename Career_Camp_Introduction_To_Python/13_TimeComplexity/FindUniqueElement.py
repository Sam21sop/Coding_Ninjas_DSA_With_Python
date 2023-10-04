from sys import stdin
from collections import Counter

def findUnique(arr, n):
    frequency_count = Counter(arr)
    for num, count in frequency_count.items():
        if count == 1:
            return num


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        result = findUnique(arr, n)
        print(result)
        t -= 1


if __name__ == '__main__':
    main()