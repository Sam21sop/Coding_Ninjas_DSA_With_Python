from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def firstIndex(array, number):
    '''Function will return first index of element if it is present in the array'''
    size = len(array)
    if size <= 0:
        return -1
    if number == array[0]:
        return 0
    result = firstIndex(array[1:], number)
    if result == -1:
        return -1
    return result+1


def take_input():
    '''Taking input form user'''
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array

def main():
    arr = take_input()
    num = int(stdin.readline().strip())
    result = firstIndex(arr, num)
    print(result)

if __name__ == '__main__':
    main()