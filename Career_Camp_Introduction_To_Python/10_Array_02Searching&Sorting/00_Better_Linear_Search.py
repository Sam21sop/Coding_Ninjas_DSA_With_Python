def sexy_search(arr, key):
    size = len(arr)
    if size < 0:
        return
    start = 0
    end = size - 1
    while start < end:
        if arr[start] == key:
            return start
        start += 1
        if arr[end] == key:
            return end
        end -= 1
    return -1


def main():
    arr = [2, 9, 3, 4,  6, 7, 8]
    key = 8
    result = sexy_search(arr, key)
    print(result)

main()