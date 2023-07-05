'''
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
'''

n = int(input())
for row in range(1, n+1):
    for col in range(1, n+1):
        print(col, end=' ')
    print()