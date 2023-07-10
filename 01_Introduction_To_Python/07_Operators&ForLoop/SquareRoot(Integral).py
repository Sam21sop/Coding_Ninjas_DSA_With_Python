def sqrt_int(num):
    ''' Return Square Root (only Intgral part)'''

    i = 1
    res = 1
    while res <= num:
        i += 1
        res = i * i
    return i-1


if __name__ == "__main__":
    n = int(input())
    result = sqrt_int(n)
    print(result)
