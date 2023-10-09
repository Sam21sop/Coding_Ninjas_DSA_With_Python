def isPrime(n):
    if n == 0 or n == 1:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#main
n = int(input('Enter a number: '))
for num in range(1, n+1):
    if isPrime(num):
        print(num)

## alterntive main
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n+1):
#         if isPrime(i):
#             print(i)


