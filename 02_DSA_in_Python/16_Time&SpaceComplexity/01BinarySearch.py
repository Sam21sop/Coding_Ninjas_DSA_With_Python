from sys import setrecursionlimit
setrecursionlimit(10**7)

def binary_search(array, start_index, end_index, key):
    if start_index > end_index:
        return False
    mid = (start_index + end_index) // 2

    if array[mid] == key:
        return True
    elif array[mid] < key:
        return binary_search(array, mid+1, end_index, key)
    else:
        return binary_search(array, start_index, mid-1, key)
    

def main():
    array = list(map(int, input().split()))
    x = int(input())
    result = binary_search(array, 0, len(array), x)
    print(result)


if __name__ == '__main__':
    main()