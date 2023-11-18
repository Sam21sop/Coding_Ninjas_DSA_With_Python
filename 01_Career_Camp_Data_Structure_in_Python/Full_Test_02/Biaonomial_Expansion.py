def bionomialCoefficient(n, k):
    if k == 0 or k == n:
        return 1
    return bionomialCoefficient(n-1, k-1) + bionomialCoefficient(n-1, k)


def bionomial_expansion_series(a, x, n):
    for k in range(n + 1):
        coefficient = bionomialCoefficient(n, k)
        term = coefficient * (a ** (n-k)) * (x**k)
        print(term, end=' ')


def main():
    a, x, n = map(int, input().split())
    bionomial_expansion_series(a, x, n)


if __name__ == '__main__':
    main()