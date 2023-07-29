def print_(n):
    if n < 0:
        return
    print(n, end=' ')
    print_(n-2)

def main():
    num = 5
    print_(num)

main()