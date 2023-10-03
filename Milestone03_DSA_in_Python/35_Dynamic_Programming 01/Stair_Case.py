from sys import stdin


def staircase(num):
    ways = [0] * (num+10)
    if num == 0:
        return 1
    if num == 1 or num == 2:
        return num
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2
    for i in range(3, (num+1)):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    return ways[num]


def main():
    num = int(stdin.readline().strip())
    res = staircase(num)
    print(res)


if __name__ == '__main__':
    main()