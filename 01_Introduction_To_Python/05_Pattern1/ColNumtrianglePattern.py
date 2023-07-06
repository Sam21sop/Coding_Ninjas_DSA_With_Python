'''
1 
1 2 
1 2 3 
1 2 3 4 
'''
n = int(input())
for row in range(1, n+1):
    for col in range(row):
        print(col+1, end=' ')
    print()