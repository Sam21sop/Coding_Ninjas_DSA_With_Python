from sys import stdin
from sys import stdin

def pair_sum_0(array):
    num_freq = {}
    count = 0
    for num in array:
        complement = -num
        if complement in num_freq:
            count += num_freq[complement]
        
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    return count
               

def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list()
    return list(map(int, stdin.readline().strip().split()))


def main():
    arr = take_input()
    res = pair_sum_0(arr)
    print(res) 


if __name__ == '__main__':
    main()     


# Input: 
# 5
# 2 1 -2 2 3

# Output:
# 2