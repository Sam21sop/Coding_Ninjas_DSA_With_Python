from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)

def binary_search_recursively(array, start, end, key):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == key:
        return mid
    elif array[mid] < key:
        return binary_search_recursively(array, mid+1, end, key)
    else:
        return binary_search_recursively(array, start, mid-1, key)
    

def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return 
    array = list(map(int, stdin.readline().strip().split()))
    return array

def main():
    arr = take_input()
    key = int(stdin.readline().strip())
    result = binary_search_recursively(arr, 0, len(arr)-1, key)
    print(result)

if __name__ == '__main__':
    main()
'''
input:
5
1 3 7 11 14
14
output:
4
'''