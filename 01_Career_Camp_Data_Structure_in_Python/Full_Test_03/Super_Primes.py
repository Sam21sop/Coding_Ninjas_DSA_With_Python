from sys import setrecursionlimit
setrecursionlimit(10**6)

def helperIsPrime(n:int, is_prime_list:[bool]):
    ''' Generate all prime number less than n using sieve'''
    is_prime_list[0] = False
    is_prime_list[1] = False

    for i in range(2, n+1):
        is_prime_list[i] = True
    
    p = 2
    while p * p <= n:
        # loop body
        if is_prime_list[p]:
            # Update all multiple of p
            for i in range(p*2, n+1, p):
                is_prime_list[i] = False
        p += 1


def super_prime(n:int):
    is_prime_list = [False] * (n+1)
    helperIsPrime(n, is_prime_list)
    primes = [0] * (n + 1)
    j = 0
    #storing all the primes generated in an array primes[]
    for p in range(2, n+1):
        if is_prime_list[p]:
            primes[j] = p
            j += 1
    
    #Print all those prime number that occupy prime number position
    for k in range(j):
        if is_prime_list[k+1]:
            print(primes[k], end=' ')


def main():
    n = int(input())
    super_prime(n)


if __name__ == '__main__':
    main()