'''
Time Complexity: O(3^N)
Space Complexity: O(N)
'''

from sys import stdin

def knapsack(weights, values, n, maxWeight):
    if n == 0 or maxWeight == 0:
        return 0
    if weights[n-1] > maxWeight:
        return knapsack(weights, values, n-1, maxWeight)
    includeItem = values[n-1] + knapsack(weights, values, n-1, maxWeight - weights[n-1])
    excludeItem = knapsack(weights, values, n-1, maxWeight)
    return max(includeItem, excludeItem)


def take_input():
    n = int(input().strip())
    if n == 0:
        return list(), list(), n, 0
    weights = list(map(int, stdin.readline().strip().split()))
    values = list(map(int, stdin.readline().strip().split()))
    maxWeight = int(input().strip())
    return weights, values, n, maxWeight


def main():
    weight, values, size, maxWeight = take_input()
    res = knapsack(weight, values, size, maxWeight)
    print(res)


if __name__ == '__main__':
    main()