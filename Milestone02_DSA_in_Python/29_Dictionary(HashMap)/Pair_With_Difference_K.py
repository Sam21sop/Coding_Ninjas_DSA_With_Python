def pair_diff_k(arr, k):
    pair_count = 0
    freq_map = {}
    for num in arr:

        if num+k in freq_map:
            pair_count += freq_map[num+k]

        if k != 0 and num-k in freq_map:
            pair_count += freq_map[num-k]

        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    return pair_count


def main():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    k = int(input())
    res = pair_diff_k(lst, k)
    print(res)


main()