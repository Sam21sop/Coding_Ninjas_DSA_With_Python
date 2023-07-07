'''
A
B C 
D E F
G H I J
'''
n = int(input())
k = ord('A')
for row in range(1, n+1):
    for col in range(row):
        print(chr(k), end=' ')
        k += 1
    print()
