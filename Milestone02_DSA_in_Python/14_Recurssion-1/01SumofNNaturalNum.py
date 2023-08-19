from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)

def sum_n_natural(number):
    if number == 0:
        return 0
    return number + sum_n_natural(number - 1)


def main():
    num = int(input())
    result = sum_n_natural(num)
    print(result)


if __name__ == '__main__':
    main()