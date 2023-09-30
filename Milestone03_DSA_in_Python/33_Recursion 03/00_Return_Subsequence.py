def subequence(input_str):
    if len(input_str) == '':
        return ''
    return subequence(input_str[1:])


def main():
    s = input()
    res = subequence(s)
    print(res)


main()