from SortingAlgo import Sorting

obj = Sorting()
array = list(map(int, input().split()))

# obj.insertion_sort(array)
# print(*array)

obj.merge_sort(array)
print(*array)
