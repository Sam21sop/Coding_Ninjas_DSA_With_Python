from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def findMin(x:int, y:int):
    ans = 0
    while y > x:
        ans += 1
        if y % 2 == 1:
            y += 1
        else:
            y //= 2
    return ans + x - y


def main():
    x, y = map(int, input().strip().split())
    print(findMin(x, y))


if __name__ == '__main__':
    main()