start = int(input())
stop = int(input())
step = int(input())

for i in range(start, stop+1, step):
    print(i, int((i-32) * 5/9))