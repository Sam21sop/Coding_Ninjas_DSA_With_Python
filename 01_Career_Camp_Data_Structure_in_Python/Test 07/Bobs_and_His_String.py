def max_distance_from_same_char(s:str):
    last_index = {}
    max_distance = -1
    for i, char in enumerate(s):
        if char in last_index:
            max_distance = max(max_distance, i - last_index[char] - 1)
        else:
            last_index[char] = i
    return max_distance


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        result = max_distance_from_same_char(s)
        print(result)


main()