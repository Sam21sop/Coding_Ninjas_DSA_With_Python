from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1) * n


def main():
    number = int(stdin.readline().strip())
    result = fact(number)
    print(result)


if __name__ == '__main__':
    main()