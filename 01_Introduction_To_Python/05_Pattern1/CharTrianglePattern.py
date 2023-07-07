'''
A
B C
C D E
D E F G
'''
n = int(input())
k = ord('A')
for row in range(1, n+1):
    for col in range(row):
        print(chr(k+col), end=' ')
    k += 1
    print()