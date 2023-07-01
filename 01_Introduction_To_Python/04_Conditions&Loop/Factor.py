n = int(input())
flag = True 
for factor in range(2, n):
    if n % factor == 0:
        print(factor, end=' ')
        flag = False
if flag:
    print(-1)