def func1(a:int, b:int):
    ans = 1
    for i in range(b):
        ans *= a
    return ans 

if __name__ == "__main__":
    # a = int(input())
    # b = int(input())
    result = func1(2, 5)
    print(result)
