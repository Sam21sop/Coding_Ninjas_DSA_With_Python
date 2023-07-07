'''
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
'''
n = int(input())
for row in range(1, n+1):
    # print space
    for space in range(n-row):
        print(' ', end=' ')

    for num in range(row):
        print(num+1, end=' ')

    for dec in range(row-1, 0, -1):
        print(dec, end=' ')
        
    print()