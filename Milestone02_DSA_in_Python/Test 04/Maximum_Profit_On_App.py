def max_profit(array):
    array.sort()
    count = 1
    max_count = -1
    for i in range(len(array)-1, -1, -1):
        current_cost = array[i] * count
        if current_cost > max_count:
            max_count = current_cost
        count += 1
    return max_count


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    mp = max_profit(arr)
    print(mp)


if __name__ == '__main__':
    main()