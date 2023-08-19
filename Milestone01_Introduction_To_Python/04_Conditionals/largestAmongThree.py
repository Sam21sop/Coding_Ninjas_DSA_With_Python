num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
num3 = int(input('Number3: '))

if num1 >= num2 and num1 >= num3:
    print(num1, 'is greter.')
elif num2 >= num3:
    print(num2, 'is greter')
else:
    print(num3, 'is greater.')