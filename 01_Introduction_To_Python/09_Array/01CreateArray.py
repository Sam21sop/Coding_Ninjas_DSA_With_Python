'''
creating array in python there are many ways.
1. using list
2. using array module 
'''

#using list
#arr = list()
arr = [1, 2, 3, 4, 5]
print(arr, type(arr))

import array
arr1 = array.array('I', [1, 1, 3, 4])
print(arr1, type(arr1))