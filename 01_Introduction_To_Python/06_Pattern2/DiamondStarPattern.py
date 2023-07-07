'''
      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
'''
n = int(input())
for row in range(1, n+1):
    for space in range(n-row):
        print(' ', end=' ')
    for asc in range(row):
        print("*", end=' ')
    for dec in range(row-1, 0, -1):
        print('*', end=' ')
    print()
for row in range(1, n):
    for space in range(row):
        print(' ', end=' ')
    for asc in range(n-row):
        print('*', end=' ')
    for dec in range(asc):
        print("*", end=' ')
    print()