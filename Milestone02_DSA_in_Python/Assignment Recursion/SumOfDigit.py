def digit_sum(number):
    d_sum = 0
    while number != 0:
        digit = number % 10
        d_sum += digit
        number //= 10
    return d_sum 


def main():
    num = int(input())
    result = digit_sum(num)
    print(result)


if __name__ == '__main__':
    main()