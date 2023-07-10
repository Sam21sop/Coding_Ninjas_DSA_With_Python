'''
432*
43*1
4*21
*321
'''

n = int(input())
for row in range(1, n+1):
    for col in range(n, 0, -1):
        if col == row:
            print('*', end='')
        else:
            print(col, end='')
    print()