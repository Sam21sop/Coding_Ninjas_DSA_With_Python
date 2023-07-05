'''
      1 
    2 3 
  4 5 6 
7 8 9 10 
'''

n = int(input())
k = 1
for row in range(1, n+1):
    for space in range(row, n):
        print(' ', end='')
    for star in range(row):
        print(k, end='')
        k += 1
    print()
    