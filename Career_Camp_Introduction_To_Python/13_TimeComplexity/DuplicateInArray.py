from sys import stdin
from collections import Counter

def findDuplicate(arr, n):
    freq_count = Counter(arr)
    for number, count in freq_count.items():
        if count >= 2:
            return number
    

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
        result = findDuplicate(arr, n)
        print(result) 
        t -= 1

if __name__ == '__main__':
    main()