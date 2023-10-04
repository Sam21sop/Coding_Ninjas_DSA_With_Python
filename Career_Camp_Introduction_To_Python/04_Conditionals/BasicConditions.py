'''
if <condition>:
    statement
elif <condition>:
    statement
else:
    statements
'''

age = int(input('Enter age: '))
#only if
if age >= 18:
    print('Your are eligible for voting.')
    print('exit only if block')


#if...else 
if age >= 18:
    print('Your are in if block')
else:
    print('your are in else block')


#if..elif..else
name = input('Enter your name: ')
if name == 'sopan':
    print('hi')
elif name == 'Python':
    print('easy to learn!')
else:
    print('enter valid input')