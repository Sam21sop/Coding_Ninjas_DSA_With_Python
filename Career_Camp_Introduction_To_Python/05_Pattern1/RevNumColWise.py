'''
4 4 4 4 
3 3 3 3 
2 2 2 2 
1 1 1 1 
'''
n = int(input())
for row in range(n, 0, -1):
    for col in range(n):
        print(row, end=' ')
    print()