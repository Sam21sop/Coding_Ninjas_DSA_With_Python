from sys import stdin

def arrayEquilibriumIndex(arr, n):
    right_sum = 0
    left_sum = 0
    for num in range(n):
        right_sum += arr[num]

    for num in range(n):
        right_sum -= arr[num]
        if right_sum == left_sum:
            return num
        left_sum += arr[num]
    return -1

def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def print_list(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        result = arrayEquilibriumIndex(arr, n)
        print(result)
        t -= 1
        

if __name__ == '__main__':
    main()