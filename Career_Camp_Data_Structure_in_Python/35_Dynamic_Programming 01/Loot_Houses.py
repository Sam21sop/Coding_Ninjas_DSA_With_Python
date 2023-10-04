from sys import stdin

def maxMoneyLooted(houses, num):
    if num == 0:
        return 0
    if num == 1:
        return houses[0]
    dp = [0] * num
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for current_house in range(2, num):
        dp[current_house] = max(dp[current_house-1], dp[current_house-2] + houses[current_house])
    return dp[num-1]
    

def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    return list(map(int, stdin.readline().strip().split())), n


def main():
    arr, size = take_input()
    res = maxMoneyLooted(arr, size)
    print(res)


if __name__ == "__main__":
    main()