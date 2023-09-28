def is_max_heap(arr_lst):
    size = len(arr_lst)
    for i in range(size):
        left_index = (2*i) + 1
        right_index = left_index + 1
        if left_index < size and arr_lst[i] < arr_lst[left_index]:
            return False
        if right_index < size and arr_lst[i] < arr_lst[right_index]:
            return False
    return True
    

def main():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    print('true') if is_max_heap(lst) else print('false')


if __name__ == '__main__':
    main()