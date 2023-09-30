def print_factorial(num, ans=1):
    if num == 0:
        print(ans)
        return
    ans *= num
    print_factorial(num-1, ans)


def main():
    num = int(input())
    print_factorial(num)


main()