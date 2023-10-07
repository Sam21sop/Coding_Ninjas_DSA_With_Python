from sys import stdin

def knapsack(weights, values, n, maxWeight):
    sub_problem_memo = [[0] * (maxWeight + 1) for _ in range(n+1)]
    for i in range(n+1):
        for w in range(maxWeight+1):
            if i == 0 or w == 0:
                sub_problem_memo[i][w] = 0
            elif weights[i-1] <= w:
                sub_problem_memo[i][w] = max(values[i-1] + sub_problem_memo[i-1][w-weights[i-1]], sub_problem_memo[i-1][w])
            else:
                sub_problem_memo[i][w] = sub_problem_memo[i-1][w]
    return sub_problem_memo[n][maxWeight]


def take_input():
    n = int(input().strip())
    if n == 0:
        return list(), list(), n, 0
    weights = list(map(int, stdin.readline().strip().split()))
    values = list(map(int, stdin.readline().strip().split()))
    maxWeight = int(input().strip())
    return weights, values, n, maxWeight


def main():
    weight, values, size, max_weight = take_input()
    res = knapsack(weight, values, size, max_weight)
    print(res)


if __name__ == "__main__":
    main()