'''
****
 ****
  ****
   ****
'''
n = int(input())

for row in range(1, n+1):
    for space in range(row-1):
        print(' ', end='')
    for col in range(n):
        print('*', end='')
    print()
