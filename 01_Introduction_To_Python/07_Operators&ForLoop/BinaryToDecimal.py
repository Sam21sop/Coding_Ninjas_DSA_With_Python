def binToDec(number):
    decimal = 0
    i = 0
    while number != 0:
        digit = number % 10
        decimal += digit * pow(2, i)
        number //= 10
        i += 1
    return decimal


if __name__ == "__main__":
    num = int(input())
    result = binToDec(num)
    print(result)