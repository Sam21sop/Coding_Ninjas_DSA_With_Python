from sys import stdin

def linearSearch(arr, n, x):
    for element in arr:
        if element == x:
            return arr.index(element)
    return -1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())
while t > 0 :
    arr, n = takeInput()
    val = int(stdin.readline().strip())
    print(linearSearch(arr, n, val))  
    t -= 1