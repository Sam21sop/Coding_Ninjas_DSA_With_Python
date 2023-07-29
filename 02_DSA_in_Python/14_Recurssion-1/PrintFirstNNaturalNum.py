def print_number(number):
    if number == 1:
        print(number, end=' ')
        return
    print_number(number-1)
    print(number, end=' ')


def take_input():
    return int(input())


def main():
    num = take_input()
    print_number(num)


if __name__ == '__main__':
    main()