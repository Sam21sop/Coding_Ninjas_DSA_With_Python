def take_input():
    lst = input().split()
    n = int(lst[0])
    m = int(lst[1])
    arr_2d = [[int(i) for i in input().split()] for _ in range(n)]
    return arr_2d

def show(arr_2d):
    for i in arr_2d:
        print(i)


arr_2d = take_input()
show(arr_2d)