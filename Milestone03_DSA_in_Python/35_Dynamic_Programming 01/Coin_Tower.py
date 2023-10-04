from sys import stdin

def findWinner(n, x, y):
    dp = [False] * (n+1)
    dp[1] = True
    for i in range(2, n+1):
        if i-1 >= 0 and not dp[i-1]:
            dp[i] = True
        if i-x >= 0 and not dp[i-x]:
            dp[i] = True
        if i-y >= 0 and not dp[i-y]:
            dp[i] = True
    return 'Beerus' if dp[n] else 'Whis'


def main():
    n, x, y = tuple(map(int, stdin.readline().strip().split()))
    res = findWinner(n, x, y)
    print(res)

if __name__ == '__main__':
    main()