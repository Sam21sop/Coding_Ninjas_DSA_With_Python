from sys import stdin

def longest_consecutive_sequence(arr):
    num_set = set(arr)
    longest_seq = []
    max_length = 0

    for num in arr:                     #Iterate ove the array
        if num-1 not in num_set:        # check wheter previous number is present or not
            current_num = num
            current_len = 1
            while current_num+1 in num_set:
                current_num += 1
                current_len += 1
            if current_len > max_length:
                max_length = current_len
                longest_seq  = [num, current_num]
    if max_length == 1:
        return [arr[0]]
    return longest_seq


def take_input():
    n = int(input())
    if n == 0:
        return list()
    return list(map(int, stdin.readline().strip().split()))


def main():
    arr = take_input()
    ans = longest_consecutive_sequence(arr)
    print(*ans)

main()

# Input:
# 13
# 2 12 9 16 10 5 3 20 25 11 1 8 6 

# Output:
# 8 12