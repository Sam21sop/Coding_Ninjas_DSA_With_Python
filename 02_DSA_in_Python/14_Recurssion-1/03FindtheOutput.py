def func(num):
    return func(num-1)

def main():
    num = 5
    ans = func(num-1)
    print(ans)

if __name__ == '__main__':
    main()