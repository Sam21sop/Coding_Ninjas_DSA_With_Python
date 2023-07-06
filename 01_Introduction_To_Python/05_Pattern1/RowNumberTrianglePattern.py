'''
1 
2 2 
3 3 3 
4 4 4 4 
'''
n = int(input())
for row in range(1, n+1):
    for col in range(row):
        print(row, end=' ')
    print()
