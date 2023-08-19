def max_sum_subarray(array, size, k):
    if size < k:
        return
    max_sum = sum(array[:k])
    current_sum = sum(array[:k])
    for i in range(k, size):
        current_sum = current_sum + array[i] - array[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum


def main():
    n, k = input().split()
    num = int(n)
    k = int(k)
    arr = list(map(int, input().split()))
    result = max_sum_subarray(arr, num, k)
    print(result)

if __name__ == '__main__':
    main()