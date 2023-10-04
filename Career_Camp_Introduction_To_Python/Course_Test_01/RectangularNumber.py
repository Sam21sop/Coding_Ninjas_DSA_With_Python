num = int(input())

for i in range(1, num+1):
    temp = num
    for j in range(1, i):
        print(temp, end=' ')
        temp -= 1
    
    for j in range(1, (2*num)-(2*i)+2):
        print(num-i+1, end=' ')

    for j in range(1, i):
        temp += 1
        print(temp, end=' ')

    print()

for i in range(num-1, 0, -1):
    temp = num
    for j in range(1, i):
        print(temp, end=' ')
        temp -= 1
    for j in range(1, (2*num)-(2*i)+2):
        print(num-i+1, end=' ')
    
    for j in range(1, i):
        temp += 1
        print(temp, end=' ')
        
    print()


