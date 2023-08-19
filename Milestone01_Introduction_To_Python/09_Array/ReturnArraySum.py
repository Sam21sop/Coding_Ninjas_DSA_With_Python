from sys import stdin

def sum_list(arr, n):
    arr_sum = 0
    for i in range(n):
        arr_sum += arr[i]
    return arr_sum
    # arr_sum = sum(arr)
    # return arr_sum


def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0 :
        arr, n = takeInput()
        if n != 0 :
            print(sum_list(arr, n))
        else :
            print(0)
        t -= 1