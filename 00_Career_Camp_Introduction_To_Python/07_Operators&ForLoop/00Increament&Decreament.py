'''
increament & decreament operator not in python instead of that we will use assignment operator.
mostly we use these operator with while loop.
example:
'''
a = 60
b = 80
if a == b:
    a += 1
    b += 1
    print(a, b)
elif a > b:
    b += 1
    print(a, b)
else:
    a += 1
    print(a, b)
