def maxPathSum(arr1, arr2, m, n):
    max_sum = 0
    current_sum1 = 0
    current_sum2 = 0
    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            current_sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            current_sum2 += arr2[j]
            j += 1
        else:
            max_sum += max(current_sum1, current_sum2) + arr1[i]
            current_sum1 = 0
            current_sum2 = 0
            i += 1
            j += 1
    while i < m:
        current_sum1 += arr1[i]
        i += 1
    while j < n:
        current_sum2 += arr2[j]
        j += 1
    max_sum += max(current_sum1, current_sum2)
    return max_sum



if __name__ == "__main__":
    m = int(input())
    ar1 = [int(i) for i in input().split(" ") if len(i)>0]
    n = int(input())
    ar2 = [int(i) for i in input().split(" ") if len(i)>0]
    print(maxPathSum(ar1, ar2, m, n))

'''
6
1 5 10 15 20 25
5
2 4 5 9 15
'''