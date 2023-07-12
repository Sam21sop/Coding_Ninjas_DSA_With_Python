def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return 'false' 
    return 'true'

if __name__ == "__main__":
   print(isPrime(47))