'''
A
A B
A B C
A B C D
'''
n = int(input())
for row in range(1, n+1):
    k = ord('A')
    for col in range(row):
        print(chr(k), end=' ')
        k += 1
    print()