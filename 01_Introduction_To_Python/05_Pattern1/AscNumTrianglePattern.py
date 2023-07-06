'''
1 
2 3 
3 4 5 
4 5 6 7 
'''
n = int(input())
for row in range(1, n+1):
    for col in range(row):
        print(row, end=' ')
        row += 1
    print()