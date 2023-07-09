'''
F(n) = F(n - 1) + F(n - 2), 
Where, F(1) = 1, F(2) = 1
'''

def fibonacci(n):
    fib_lst = [0, 1]
    for num in range(2, n+1):
        fib_lst.append(fib_lst[num-2] + fib_lst[num-1])
    return fib_lst[n]

if __name__ == '__main__':
    n = int(input())
    result = fibonacci(n)
    print(result)

