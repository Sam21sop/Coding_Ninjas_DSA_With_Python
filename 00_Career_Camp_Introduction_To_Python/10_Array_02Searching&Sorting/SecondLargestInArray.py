from sys import stdin
MIN_VALUE = -2147483648


def second_large(array:list[int]):
    '''Function return the second large element.'''
    array.sort()
    return array[-2]


def second_largest_element(array:list[int], size:int):
    '''Function return the second large element.'''
    if size == 0:
        return MIN_VALUE
    largest_ele = array[0]
    second_large_ele = MIN_VALUE
    for i in range(size):
        if largest_ele < array[i]:
            second_large_ele = largest_ele
            largest_ele = array[i]
        elif second_large_ele < array[i] and array[i] != largest_ele:
            second_large_ele = array[i]
    return second_large_ele


def take_input():
    '''Function take input from user.'''
    num = int(stdin.readline().rstrip())
    if num == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, num

if __name__ == '__main__':
    arr, n = take_input()
    result =  second_largest_element(arr, n)
    print(result)
    