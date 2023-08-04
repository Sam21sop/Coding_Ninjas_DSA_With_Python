from sys import setrecursionlimit
setrecursionlimit(11000)


def multiplication(m, n):
    if n == 0 or m == 0:
        return 0
    if n > 0:
        return m + multiplication(m, n-1)
    else:
        return m - multiplication(m, n+1)


def main():
    m = int(input())
    n = int(input())
    ans = multiplication(m, n)
    print(ans)

if __name__ == '__main__':
    main()