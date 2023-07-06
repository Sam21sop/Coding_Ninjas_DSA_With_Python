'''
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4 
'''
n = int(input())
for row in range(n):
    for col in range(n):
        print(row+1, end=' ')
    print()
