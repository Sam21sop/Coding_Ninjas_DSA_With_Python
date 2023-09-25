from collections import Counter

def remove_duplicates(arr):
    frequency_count = Counter(arr)
    for i in arr:
        if frequency_count[i] > 1:
            del frequency_count[i]
    return list(frequency_count.keys())


print(*remove_duplicates([1, 1, 9, 2, 3, 2, 3, 4, 5, 5]))