from collections import Counter
from sys import stdin


def max_frequency_num(arr):
    frequency = Counter(arr)
    ans = arr[0]
    for num in arr:
        if frequency[num] > frequency[ans]:
            ans = num
    return ans


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return [], 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr


def main():
    arr = take_input()
    print(max_frequency_num(arr))


main()


# Input:
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6 

# Output: 
# 2