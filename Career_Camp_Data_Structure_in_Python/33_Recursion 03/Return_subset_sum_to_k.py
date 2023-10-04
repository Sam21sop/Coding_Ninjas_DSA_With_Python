from sys import stdin, setrecursionlimit
setrecursionlimit(100*6)


def subset_sum_k_helper(array, start_index, k):
    if len(array) == start_index:
        if k == 0:
            return [list()]
        else:
            return list()
    small_output_1 = subset_sum_k_helper(array, start_index+1, k)
    small_output_2 = subset_sum_k_helper(array, start_index+1, k - array[start_index])
    output = (len(small_output_1) + len(small_output_2)) * [0]
    index = 0
    for i in range(len(small_output_1)):
        output[index] = small_output_1[i]
        index += 1
    for i in range(len(small_output_2)):
        output[index] = (len(small_output_2[i]) + 1) * [0]
        output[index][0] = array[start_index]
        for j in range(len(small_output_2[i])):
            output[index][j+1] = small_output_2[i][j]
        index += 1
    return output


def subset_sum_k(array, k):
    return subset_sum_k_helper(array, 0, k)


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list()
    return list(map(int, stdin.readline().strip().split()))


def display(lst_of_lst):
    for lst in lst_of_lst:
        for elem in lst:
            print(elem, end=' ')
        print()


def main():
    lst = take_input()
    if len(lst) != 0:
        k = int(input())
        lst_of_lst = subset_sum_k(lst, k)
        display(lst_of_lst)


if __name__ == "__main__":
    main()