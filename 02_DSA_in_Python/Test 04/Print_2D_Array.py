'''
Given a 2D integer array with n rows and m columns. 
Print the 0th row from input n times, 
1st row n-1 times…..(n-1)th row will be printed 1 time.
'''

def print_2d_array(rows, columns):
    for i in range(rows):
        matrix = list(map(int, input().split()))
        for j in range(columns, 0, -1):
            print(*matrix)
        columns -= 1


def main():
    n, m = input().split()
    r = int(n)
    c = int(m)
    print_2d_array(r, c)


if __name__ == '__main__':
    main()

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9