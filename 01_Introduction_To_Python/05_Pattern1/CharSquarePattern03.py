'''
A B C D 
A B C D 
A B C D 
A B C D 
'''
n = int(input())
for row in range(n):
    k = ord('A')
    for col in range(n):
        print(chr(k), end=' ')
        k += 1
    print()

