'''
A B C D 
E F G H 
I J K L 
M N O P 
'''
n = int(input())
k = ord('A')
for row in range(n):
    for col in range(n):
        print(chr(k), end=' ')
        k += 1
    print()