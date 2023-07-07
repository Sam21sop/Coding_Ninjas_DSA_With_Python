'''
  *
 ***
*****
 ***
  *
'''
n = int(input())
for row in range(1, n+1, 2):
    for spaces in range(n-row):
        print(' ', end='')
    for star in range(row):
        print('*', end='')
    print()


for row in range(n-1, 0, -2):
    for spaces in range(n,  row, -1):
        print(' ', end='')
    for star in range(row-1, 0, -1):
        print('*', end='')
    print()