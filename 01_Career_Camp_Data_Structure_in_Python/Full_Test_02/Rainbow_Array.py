def isRainbow(arr, arr_size):
    if arr_size < 13:
        print('no')
        return
    start = 0
    end = arr_size - 1
    is_valid = True
    current = 0
    while start != end and start < end:
        if arr[start] != arr[end]:
            is_valid = False
            break
        if arr[start] < 1 or arr[start] > 7:
            is_valid = False
            break
        if arr[start] != current:
            if arr[start] != current + 1:
                is_valid = False
                break
            else:
                current = arr[start]
        start += 1
        end -= 1
    if (arr[start] == 7 or current == 7) and  is_valid:
        print('yes')
    else:
        print('no')


def main():
    arr_size = int(input())
    array = list(map(int, input().strip().split()))
    isRainbow(array, arr_size)


if __name__ == '__main__':
    main()