frequency_dict = {}

def custom_sort(item):
    return (-frequency_dict[item], item)

def main():
    n = int(input())
    array = list(map(int, input().split()))
    for num in array:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    array.sort(key=custom_sort)
    print(*array)   


if __name__ == '__main__':
    main()