'''
4 3 2 1
3 2 1
2 1
1
'''
n = int(input())
for row in range(1, n+1):
    for col in range(n-row+1, 0, -1):
        print(col, end=' ')
    print()