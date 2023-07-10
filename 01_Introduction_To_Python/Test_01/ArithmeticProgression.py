def is_AP(lst, num):
    ''' Function check the arithmetic progression and return boolean value'''
    if num == 1:
        return True
    lst.sort()
    d = lst[1] - lst[0]
    for i in range(2, n):
        if lst[i] - lst[i-1] != d:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    num_lst = list(map(int, input().split()))
    if is_AP(num_lst, n):
        print('true')
    else:
        print('false')

