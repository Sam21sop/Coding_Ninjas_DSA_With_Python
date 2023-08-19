'''
Range() function work on only integer
syantax: range(start, stop, step)
start: where do you want to the start the loop. (included)
stop: where do you want to stop the loop. (excluded)
step: it work like increement, by default is 1
'''
#increement
for i in range(1, 11, 1):
    print(i, end=' ')
print()

#decreement
for i in range(10, 0, -1):
    print(i, end=' ')
print()