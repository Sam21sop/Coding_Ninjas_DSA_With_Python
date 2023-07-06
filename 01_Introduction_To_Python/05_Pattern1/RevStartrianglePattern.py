'''
      * 
    * * 
  * * * 
* * * * 
'''
n = int(input())
for row in range(1, n+1):
    # printing spaces
    for space in range(n-row, 0, -1):
        print(' ', end=' ')

    #printing stars
    for num in range(row):
        print('*', end=' ')

    #next line
    print()