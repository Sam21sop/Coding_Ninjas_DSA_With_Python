'''
1234554321
1234**4321
123****321
12******21
1********1
'''

n = int(input())
for row in range(n):
    for num in range(n-row):
        print(num+1, end='')
    for star in range(row):
        print('**', end='')
    for dec in range(n-row, 0, -1):
        print(dec, end='')
    print()