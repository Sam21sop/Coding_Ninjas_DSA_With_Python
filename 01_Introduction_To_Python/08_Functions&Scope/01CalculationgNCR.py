'''
nCr = n! / r!(n-r)!
'''
def fact(n):
    '''Function return the factorial of number'''
    if n == 0 or n == 1:
        return n
    return n * fact(n-1)


def NCR(n, r):
    '''Function return the combination'''
    n_fact = fact(n)
    r_fact = fact(r)
    nr_fact = fact(n-r)
    ncr = int(n_fact / (r_fact * nr_fact))
    return ncr 

if __name__ == "__main__":
    n = int(input())
    r = int(input())
    result = NCR(n, r)
    print(result)
