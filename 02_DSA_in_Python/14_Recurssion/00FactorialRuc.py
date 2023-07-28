def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def main():
    number = int(input())
    result = fact(number)
    print(result)


if __name__ == '__main__':
    main()