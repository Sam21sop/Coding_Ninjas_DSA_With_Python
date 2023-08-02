from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def merge(array, l, m, r):
    num1 = m - l + 1
    num2 = r - m

    #create Two temp array
    R = [0] * num2
    L = [0] * num1

    #copy data to temp array
    for i in range(num1):
        L[i] = array[l+i]
    for j in range(num2):
        R[j] = array[m+j+1]

    #merged the temp array back
    i = 0
    j = 0
    k = l
    while i < num1 and j < num2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < num1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < num2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(array, l, r):
    if l < r:
        m = (l+r) // 2
        merge_sort(array, l, m)
        merge_sort(array, m+1, r)

        #merging two sorted array
        merge(array, l, m, r)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return [], 0
    array = list(map(int, stdin.readline().strip().split()))
    return array


def main():
    arr = take_input()
    merge_sort(arr, 0, len(arr)-1)
    print(*arr)


if __name__ == '__main__':
    main()