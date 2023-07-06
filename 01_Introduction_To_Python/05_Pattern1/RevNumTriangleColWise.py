'''
      1 
    2 2 
  3 3 3 
4 4 4 4
'''
n = int(input())
for row in range(1, n+1):
    for space in range(n-row, 0, -1):
        print(' ', end=' ')
    for num in range(row):
        print(row, end=' ')
    print()