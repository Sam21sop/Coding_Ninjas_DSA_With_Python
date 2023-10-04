def subset_sum(arr):
    cumulative_sum = 0
    max_length = 0
    cumulative_sum_map = {}
    for i, num in enumerate(arr):
        cumulative_sum += num
        if cumulative_sum == 0:
            max_length = i + 1

        if cumulative_sum in cumulative_sum_map:
            max_length = max(max_length, i - cumulative_sum_map[cumulative_sum])
        else:
            cumulative_sum_map[cumulative_sum] = i
    return max_length


def main():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    res = subset_sum(lst)
    print(res)


main()


# Input:
# 10 
# 95 -97 -387 -435 -5 -70 897 127 23 284

# Output:
# 5