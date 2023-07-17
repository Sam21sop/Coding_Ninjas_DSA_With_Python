from sys import stdin

def pairSum(arr, n, x):
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == x:
                num += 1
    return num


def takeInput() :
    '''Taking Input Using Fast I/O'''
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0 :
        arr, n = takeInput()
        x = int(stdin.readline().strip())
        print(pairSum(arr, n, x))
        t -= 1