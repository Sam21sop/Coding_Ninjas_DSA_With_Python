'''
Python has advance data type:

1. list         ---> (list())
2. tuple        ---> (tuple())
3. set          ---> (set())
4. dictionary   ---> (dict())
'''

#list data type
lst = [10, 99.99, 'python', True, 4+5j]
print(lst, type(lst))

#tuple data type
tup = (10, 99.99, 'python', True, 4+5j)
print(tup, type(tup))

#set data type
s = {10, 'python', True, 99.9}
print(s, type(s))

#dictionary data type
d = {'name':'Python', 'year':1991, 'version':3.10}
print(d, type(d))