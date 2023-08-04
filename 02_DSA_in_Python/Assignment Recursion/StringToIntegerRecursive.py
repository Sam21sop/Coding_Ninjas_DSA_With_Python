def string_to_int(strings):
    if len(strings) == 1:
        return ord(strings[0]) - ord('0')
    small_string = string_to_int(strings[1:])
    result = ord(strings[0]) - ord('0')
    result = result * (10 ** (len(strings)-1)) + small_string
    return result


def main():
    s = input()
    ans = string_to_int(s)
    print(ans)


if __name__ == '__main__':
    main()