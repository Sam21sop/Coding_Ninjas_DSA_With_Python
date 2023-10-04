from sys import setrecursionlimit
setrecursionlimit(10**7)

def replace_char(strings, old_char, new_char):
    if strings == '':
        return ''
    small_string = replace_char(strings[1:], old_char, new_char)
    if strings[0] == old_char:
        return new_char + small_string
    else:
        return strings[0] + small_string
    

def main():
    result = replace_char('abcxdxex', 'x', 'y')
    print(result)


if __name__ == "__main__":
    main()