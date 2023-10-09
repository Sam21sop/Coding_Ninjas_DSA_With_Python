'''
      1 
    1 2 
  1 2 3 
1 2 3 4 
'''
n = int(input())
for row in range(1, n+1):
    # printing spaces
    for space in range(n-row, 0, -1):
        print(' ', end=' ')

    #printing stars
    for num in range(row):
        print(num+1, end=' ')

    #next line
    print()