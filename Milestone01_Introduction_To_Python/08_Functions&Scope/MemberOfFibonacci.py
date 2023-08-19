def member_fibonacci(num):
    '''Function check the number is member of fibonacci'''
    lst = [0, 1]
    for n in range(2, num+1):
        lst.append(lst[n-1] + lst[n-2])
    if num in lst:
        return 'true'
    return 'false'
    

if __name__ == "__main__":
    n = int(input())
    result = member_fibonacci(n)
    print(result)
