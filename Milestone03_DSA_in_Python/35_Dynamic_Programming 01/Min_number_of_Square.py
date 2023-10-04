from sys import stdin

def minCount(num):
    dp = [float('inf')] * (num+10)
    dp[0] = 0
    for i in range(1, num+1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[num]

def main():
    num = int(input())
    res = minCount(num)
    print(res)

main()