#Method resolution algorithm
def sum_n(a:float, b:float):
    return f'long sum {a+b}'

def sum_n(a:int, b:int):
    return f'int sum {a+b}'

# if __name__ == '__main__':
#     a = 4
#     b = 5
#     print(sum_n(a, b))

a = 4
b = 5
print(sum_n(a, b))