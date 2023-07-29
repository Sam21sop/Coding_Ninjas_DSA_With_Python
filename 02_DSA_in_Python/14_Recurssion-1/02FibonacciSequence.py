def fib_series(number):
    if number <= 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    else:
        sequence = fib_series(number-1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence


def main():
    num = int(input())
    result = fib_series(num)
    print(*result)

if __name__ == '__main__':
    main()