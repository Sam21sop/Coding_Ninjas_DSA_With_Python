def split_arr(array, i, total_sum):
    if i == len(array):
        if total_sum == 0:
            return True
        else:
            return False
    
    if array[i] % 5 == 0:
        return split_arr(array, i+1, total_sum+array[i])
    elif array[i] % 3 == 0:
        return split_arr(array, i+1, total_sum-array[i])
    else:
        result1 = split_arr(array, i+1, total_sum+array[i])
        result2 = split_arr(array, i+1, total_sum-array[i])
        return result1 or result2


def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = split_arr(arr, 0, 0)
    if ans:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()