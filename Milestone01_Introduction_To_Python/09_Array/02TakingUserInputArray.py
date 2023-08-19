from array import array

n = input('Enter number of element: ')
elements = list(map(int, input().split()))
arr = array('I', elements)
for i in arr:
    print(i, end=' ')