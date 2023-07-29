from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def digitCount(number):
    if number // 10 == 0:
        return 1
    return 1 + digitCount(number-1)

def take_input():
    return int(stdin.readline().strip())


def main():
    n = take_input()
    result = digitCount(n)
    print(result)


if __name__ == '__main__':
    main()

