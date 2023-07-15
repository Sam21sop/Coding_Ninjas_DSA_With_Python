from sys import stdin

def swap_alternate(arr, n):
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]


def take_input():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().rstrip().split(' ')))
    return arr, n


def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

if __name__ == '__main__':
    t = int(stdin.readline().rstrip())
    while t > 0:
        arr, n = take_input()
        if n != 0:
            swap_alternate(arr, n)
            print_arr(arr, n)
        t -= 1
