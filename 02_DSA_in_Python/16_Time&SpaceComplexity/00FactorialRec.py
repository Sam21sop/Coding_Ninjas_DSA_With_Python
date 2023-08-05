from sys import setrecursionlimit
setrecursionlimit(10**7)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def main():
    num = int(input())
    ans = fact(num)
    print(ans)

if __name__ == '__main__':
    main()