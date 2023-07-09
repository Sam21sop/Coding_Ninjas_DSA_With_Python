def sumOrProduct(n, c):
    '''
    n: number by user defined
    c: user choice
    '''
    s = 0
    p = 1
    for num in range(1, n+1):
        s += num
        p *= num
    
    if c == 1:
        return s
    elif c == 2:
        return p 
    else:
        return -1
    
    
if __name__ == "__main__":
    number = int(input())
    choice = int(input())
    result = sumOrProduct(number, choice)
    print(result)