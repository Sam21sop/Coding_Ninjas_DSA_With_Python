from sys import setrecursionlimit
setrecursionlimit(11000)


def count_zeros(number):
    if number < 0:
        # make a number positive
        number *= -1
    if number < 10:
        if number == 0:
            return 1
        return 0
    rem_number = count_zeros(number // 10)
    if number % 10 == 0:
        rem_number += 1
    return rem_number


def main():
    num = int(input())
    ans = count_zeros(num)
    print(ans)


if __name__ == '__main__':
    main()