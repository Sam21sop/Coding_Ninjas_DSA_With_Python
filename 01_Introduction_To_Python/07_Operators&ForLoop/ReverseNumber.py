def revNum(num):
    reverse_number = 0
    while num != 0:
        digit = num % 10
        reverse_number = reverse_number * 10 + digit
        num //= 10
    return reverse_number


if __name__ == "__main__":
    n = int(input())
    result = revNum(n)
    print(result)