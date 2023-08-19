from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def checkNumber(array, size, x):
    if size <= 0:
        return 'false'
    if array[size-1] == x:
        return 'true'
    return checkNumber(array, size-1, x)


def take_input():
    n = int(stdin.readline().strip())
    if n <= 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n
    

def main():
    arr, size = take_input()
    number = int(stdin.readline().strip())
    result = checkNumber(arr, size, number)
    print(result)


if __name__ == '__main__':
    main()