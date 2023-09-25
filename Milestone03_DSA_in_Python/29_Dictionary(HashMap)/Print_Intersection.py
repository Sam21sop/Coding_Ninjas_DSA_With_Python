from sys import stdin

def intersection(arr1, arr2) :
    arr1_frequency = {}                                         #create empty dictionary
    for key in arr1:                                            # add element of arr1 in dictionary
        if key in arr1_frequency:
            arr1_frequency[key] += 1
        else:
            arr1_frequency[key] = 1
    intersection = []                                           #create empty list for list
    for num in arr2:                                            # iterate over the arr2
        if num in arr1_frequency and arr1_frequency[num] > 0:   # Find intersection    
            intersection.append(num)
            arr1_frequency[num] -= 1     
    intersection.sort()                                         #sort intersection list
    print(*intersection)                                        # print intersection


def take_input():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr

def main():
    num_of_test_case = int(stdin.readline().strip())
    for _ in range(num_of_test_case):
        arr1 = take_input()
        arr2 = take_input()
        intersection(arr1, arr2)
        print()

main()


# Input
# Testcase: 1
# arr1_size: 4        
# arr1_elem: 2 6 1 2  
# arr2_size: 5        
# arr2_elem: 1 2 3 4 2

# Output: 1 2 2