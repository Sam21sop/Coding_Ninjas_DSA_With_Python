from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def power_rec(x, n):
    if n == 0:
        return 1
    return x * power_rec(x, n-1)


def take_input():
    l = stdin.readline().strip().split()
    x = int(l[0])
    n = int(l[1])
    return x, n


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        a, b = take_input()
        result = power_rec(a, b)
        print(result)
        t -= 1


if __name__ == '__main__':
    main()
