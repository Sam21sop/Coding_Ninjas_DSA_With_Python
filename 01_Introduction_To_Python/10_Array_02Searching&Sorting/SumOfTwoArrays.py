from sys import stdin

def two_array_sum(array1:list[int], size1:int, array2:list[int], size2:int, output:list[int]):
    i = size1 - 1
    j = size2 - 1
    k = max(size1, size2)
    carry = 0
    while i >= 0 and j >= 0:
        SUM = array1[i] + array2[j] + carry
        output[k] = SUM % 10
        carry = SUM // 10
        i -= 1
        j -= 1
        k -= 1

    while i >= 0:
        SUM = array1[i] + carry
        output[k] = SUM % 10
        carry = SUM % 10
        i -= 1
        k -= 1

    while j >= 0:
        SUM = array2[j] + carry
        output[k] = SUM % 10
        carry = SUM // 10
        j -= 1
        k -= 1
    output[0] = carry



def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def print_list(array, size):
    for i in range(size):
        print(array[i], end=' ')
    print()


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    while t > 0:
        arr1, n = take_input()
        arr2, m = take_input()
        output = (max(n, m) + 1) * [0]
        two_array_sum(arr1, n, arr2, m, output)
        print_list(output, len(output))
        t -= 1
        