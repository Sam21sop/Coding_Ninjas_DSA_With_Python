from sys import setrecursionlimit
setrecursionlimit(10**7)

def geometric_sum(k):
    if k == 0:
        return 1
    return 1/pow(2, k) + geometric_sum(k-1)


def main():
    n = int(input())
    print("%.5f" %geometric_sum(n))


if __name__ == '__main__':
    main()