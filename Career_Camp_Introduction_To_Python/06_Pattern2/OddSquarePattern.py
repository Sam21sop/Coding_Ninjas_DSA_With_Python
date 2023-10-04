''' 
1357
3571
5713
7135
'''
n = int(input())

for row in range(1, n+1):
    value = (2 * row) - 1
    max_value = (2 * n) - 1
    for col in range(1, n+1):
        print(value, end='')
        value += 2
        if value > max_value:
            value = 1
    print()