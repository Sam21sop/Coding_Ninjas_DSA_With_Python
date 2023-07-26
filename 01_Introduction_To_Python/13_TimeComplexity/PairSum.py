from sys import stdin


def pairSum(arr, n, num):
    #sort the array
    arr.sort()

    start_index = 0
    end_index = n-1
    num_pair_count = 0

    while start_index < end_index:
        #checking start & end addition is
        
        # less than num then increment start_index
        if arr[start_index] + arr[end_index] < num:
            start_index += 1
        
        # is greater than num then decrement end_index
        elif arr[start_index] + arr[end_index] > num:
            end_index -= 1

        #else
        else:
            element_at_start = arr[start_index]
            element_at_last = arr[end_index]

            #check whether start and end element are equal or not
            if element_at_start == element_at_last:
                total_element = (end_index - start_index) + 1
                num_pair_count += (total_element * (total_element-1)//2)
                return num_pair_count
            
            #initialize temp_start and temp_end
            temp_start = start_index + 1
            temp_end = end_index - 1

            while (temp_start <= temp_end) and (arr[temp_start] == element_at_start):
                temp_start += 1
            
            while (temp_end >= temp_start) and (arr[temp_end] == element_at_last):
                temp_end -= 1
            
            total_element_at_start = temp_start - start_index
            total_element_at_last = end_index - temp_end

            num_pair_count += (total_element_at_start * total_element_at_last)

            start_index = temp_start
            end_index = temp_end
    return num_pair_count    


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    array = list(map(int, stdin.readline().strip().split()))
    return array, n


def main():
    t = int(stdin.readline().strip())
    while t > 0:
        arr, n = take_input()
        num = int(stdin.readline().strip())
        result = pairSum(arr, n, num)
        print(result)
        t -= 1


if __name__ == '__main__':
    main()