import sys


def findUnique(arr, n) :
    unique_count = 1
    for i in range(n):
        if arr.count(arr[i]) > unique_count:
            unique_count = arr.count(arr[i])
            res = arr[i]
    return res



#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())
while t > 0 :
    arr, n = takeInput()
    print(findUnique(arr, n))
    t -= 1