from sys import stdin, setrecursionlimit, maxsize as MAX_VALUE
setrecursionlimit(10**6)


def minsteps_to_one(num):
    if num == 1:
        return 0
    
    subtract_by_one = MAX_VALUE
    divide_by_two = MAX_VALUE
    divide_by_three = MAX_VALUE

    subtract_by_one = minsteps_to_one(num-1)
    if num % 2 == 0:
        divide_by_two = minsteps_to_one(num // 2)
    if num % 3 == 0:
        divide_by_three = minsteps_to_one(num // 3)
    return 1 + min(subtract_by_one, divide_by_two, divide_by_three)


def main():
    n = int(stdin.readline().strip())
    res = minsteps_to_one(n)
    print(res)


if __name__ == '__main__':
    main()