from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def max_doller(num, memo):
    if num <= 11:
        return num
    if num in memo:
        return memo[num]
    max_value = max(num, max_doller(num//2, memo) + max_doller(num//3, memo) + max_doller(num//4, memo))
    memo[num] = max_value
    return max_value


def byteLandian(num):
    memo = {}
    return max_doller(num, memo)


def main():
    n = int(input())
    res = byteLandian(n)
    print(res)

if __name__ == "__main__":
    main()