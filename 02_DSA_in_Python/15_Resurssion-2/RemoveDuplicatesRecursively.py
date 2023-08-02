from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def remove_consecutive_duplicates(strings):
    if len(strings) <= 1:
        return strings
    if strings[0] == strings[1]:
        return remove_consecutive_duplicates(strings[1:])
    else:
        return strings[0] + remove_consecutive_duplicates(strings[1:])
    

def main():
    strings = input().strip()
    result = remove_consecutive_duplicates(strings)
    print(result)


if __name__ == '__main__':
    main()