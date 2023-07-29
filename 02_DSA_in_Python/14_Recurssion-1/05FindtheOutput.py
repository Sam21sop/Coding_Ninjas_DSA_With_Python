def show(n):
    if n < 0:
        return
    if n == 0:
        print(n)
        return
    show(n-1)
    print(n, end=' ')

def main():
    num = 3
    show(num)

main()