def duplicatesNumber(arr):
    count = 1
    for number in arr:
        if arr.count(number) > count:
            result = number
    return result

if __name__ == '__main__':
    n = int(input('Number of Element: '))
    arr = []
    for i in range(n):
        arr.append(input())
    print(duplicatesNumber(arr))