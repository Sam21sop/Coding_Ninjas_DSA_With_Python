from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def staircase_recursive(num):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        return staircase_recursive(num - 1) + staircase_recursive(num - 2) + staircase_recursive(num - 3)
    

def main():
    num = int(input())
    res = staircase_recursive(num)
    print(res)


if __name__ == '__main__':
    main()