from sys import stdin


def swap_element(array:list[int], start_idx, end_idx):
    '''Swap the element in the list'''
    array[start_idx], array[end_idx] = array[end_idx], array[start_idx]


def sort012(array:list[int], size:int):
    '''Function sort the list of 0 1 2'''
    next_zero = 0
    next_two = size - 1
    i = 0
    while i <= next_two:
        if array[i] == 0:
            swap_element(array, next_zero, i)
            i += 1
            next_zero += 1

        elif array[i] == 2:
            swap_element(array, next_two, i)
            next_two -= 1

        else:
            i += 1


def take_input():
    '''Function will take user input'''
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def print_list(array:list[int], size:int):
    '''function will print the sorted list'''
    for i in range(size):
        print(array[i], end=' ')
    print()


if __name__ == "__main__":
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        sort012(arr, n)
        print_list(arr, n)
        t -= 1