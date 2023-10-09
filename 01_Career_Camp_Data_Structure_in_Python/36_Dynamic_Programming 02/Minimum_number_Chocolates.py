from sys import stdin

def getMin(arr, n):
    chocolates = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            chocolates[i] = chocolates[i-1] + 1
    
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1] and chocolates[i] <= chocolates[i+1]:
            chocolates[i] = chocolates[i+1] + 1

    return sum(chocolates)


def takeInput():
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n


def main():
    arr,n=takeInput()
    print(getMin(arr,n))

if __name__ == '__main__':
    main()