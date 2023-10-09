from sys import stdin

def issubsetPresent(arr, arr_size, target_sum):
    subproblem_memo = [[False] * (target_sum + 1) for _ in range(arr_size + 1)]
    for i in range(arr_size + 1):
        subproblem_memo[i][0] = True

    for i in range(1, arr_size + 1):
        for j in range(1, target_sum + 1):
            if arr[i-1] <= j:
                subproblem_memo[i][j] = subproblem_memo[i-1][j] or subproblem_memo[i-1][j-arr[i-1]]
            else:
                subproblem_memo[i][j] = subproblem_memo[i-1][j]
    
    return subproblem_memo[arr_size][target_sum]


def take_input():
    n = int(input())
    if n == 0:
        return list(), 0
    return list(map(int, input().strip().split())), n, int(input().strip())


def main():
    arr, size, target = take_input()
    if issubsetPresent(arr, size, target):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()