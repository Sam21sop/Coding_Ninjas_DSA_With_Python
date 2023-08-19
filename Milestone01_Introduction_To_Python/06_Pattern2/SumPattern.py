'''
1=1
1+2=3
1+2+3=6
1+2+3+4=10
'''
n = int(input())
s = 0
for row in range(1, n+1):
    s += row 
    for col in range(1, row+1):
        print(col, end='')
        if row == col:
            print('=', end='')
        else:
            print('+', end='')
    print(s)