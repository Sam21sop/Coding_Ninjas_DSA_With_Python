def factorial(num):
    '''Function Return Factorial of Number'''
    fact = 1
    for i in range(2, num+1):
        fact *= i 
    return fact 

def probability(n, x):
    n0 = factorial(8) / (factorial(n*1) * factorial(8-n))
    n1 = factorial(4) / (factorial(x*1) * factorial(4-x))
    n2 = factorial(4) / (factorial((n-x)*1) * factorial(4-(n-x)))
    pe = ((n1 * n2) / n0) * 100 
    return int(pe)

def main():
    n, x = input().split()
    n = int(n)
    x = int(x)
    res = probability(n, x)
    print(res)

if __name__ == '__main__':
    main()