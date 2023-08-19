'''
4 4 4 4
3 3 3
2 2
1
'''

n = int(input())
for row in range(1, n+1):
    for col in range(n, 0, -1):
        print(n, end=' ')
    n -= 1
    print()