'''
A A A A 
B B B B 
C C C C 
D D D D 
'''
n = int(input())
char = ord('A')
for row in range(n):
    for col in range(n):
        print(chr(char), end=' ')
    char += 1
    print()