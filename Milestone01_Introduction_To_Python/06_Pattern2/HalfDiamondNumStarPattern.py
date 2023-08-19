'''
*
*1*
*121*
*12321*
*1234321*
*12321*
*121*
*1*
*
'''
n = int(input())

print('*')
for row in range(1, n+1):
    print('*', end='')
    for num in range(row):
        print(num+1, end='')
    for dec in range(row-1, 0, -1):
        print(dec, end='')
    print('*')

for row in range(2, n+1):
    print('*', end='')
    for col in range(n-row+1):
        print(col+1, end='')
    for dec in range(col, 0, -1):
        print(dec, end='')
    print("*")
print('*')