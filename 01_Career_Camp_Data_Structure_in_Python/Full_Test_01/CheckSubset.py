'''
Given two integer array. check if second array is a subset of first array.
'''

def is_subset(arr1, n1, arr2, n2):
    if n1 < 0 or n2 < 0 or n1 < n2:
        return False
    set1 = set(arr1)
    set2 = set(arr2)
    return set2.issubset(set1)

def main():
    n1 = int(input())
    arr1 = list(map(int, input().strip().split()))
    n2 = int(input())
    arr2 = list(map(int, input().strip().split()))
    result = is_subset(arr1, n1, arr2, n2)
    if result:
        print('true')
    else:
        print('false')

if __name__ == '__main__':
    main()