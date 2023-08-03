def is_palindrom(string):
    size = len(string)
    if size <= 1:
        return True
    if string[0] != string[size-1]:
        return False
    return is_palindrom(string[1:-1])


def main():
    strings = input().strip()
    ans = is_palindrom(strings)
    print(ans)


if __name__ == '__main__':
    main()