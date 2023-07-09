'''
break: it is used to break the imediate loop
'''
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)



for j in range(1, 10):
    for i in range(2, 6, 2):
        if i == 6:
            break
        print('inner loop')
    print('**Outer loop**')