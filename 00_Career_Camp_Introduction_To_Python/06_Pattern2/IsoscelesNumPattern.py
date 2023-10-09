'''
      1 
    2 3 2 
  3 4 5 4 3 
4 5 6 7 6 5 4 
'''

n = int(input())

for row in range(1, n+1):
    for space in range(n-row):
        print(' ', end=' ')

    for asc in range(row):
        print(asc+row, end=' ')
        
    for dec in range(row-1, 0, -1):
        print(dec+row-1, end=' ')

    print()