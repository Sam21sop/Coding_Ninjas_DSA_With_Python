def largest_element(arr):
    return max(arr)

def smallest_element(arr):
    return min(arr)

if __name__ == '__main__':
    arr = list(map(int, input().split()))

    largest = largest_element(arr)
    print(largest)
    
    smallest = smallest_element(arr)
    print(smallest)