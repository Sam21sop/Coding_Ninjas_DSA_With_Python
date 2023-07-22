from sys import stdin

def total_sum(array, size):
    total_s = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i == 0) or (j == 0) or (i == j) or (i == len(array)-1) or (j == len(array[i])-1) or (i+j == len(array)-1):
                total_s += array[i][j]
    print(total_s)


def take_2d_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    matrix = [list(map(int, stdin.readline().strip().split())) for row in range(n)]
    return matrix, n

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_2d_input()
        total_sum(arr, n)
        t -= 1