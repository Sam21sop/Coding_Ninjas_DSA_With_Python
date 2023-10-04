def print_subset_sum_to_k(array, target_sum, current_sum, current_subset, index):
    if len(array) == index:
        if current_sum == target_sum:
            print(' '.join(map(str, current_subset)))
        return
    
    #include current element in the subset
    new_subset = current_subset + [array[index]]
    print_subset_sum_to_k(array, target_sum, current_sum+array[index], new_subset, index+1)

    #excluded current element in the subset
    print_subset_sum_to_k(array, target_sum, current_sum, current_subset, index+1)


def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    print_subset_sum_to_k(array=arr, target_sum=k, current_sum=0, current_subset=[], index=0)


if __name__ == '__main__':
    main()