#check the error
'''
def func(a:int):
    b = a
    b += 10


if __name__ == "__main__":
    a = 10
    func(a)
    print(b)
#output: YES
'''
###############################
def func(a:int):
    b = a
    b += 10


if __name__ == "__main__":
    a = 10
    func(a)
    print(a)

#output: NO
