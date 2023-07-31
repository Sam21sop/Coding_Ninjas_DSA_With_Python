def replace_pi(strings):
    '''Replace "pi" with "3.14" by recursively'''
    if len(strings) <= 1:
        return strings
    if strings[0] == 'p' and strings[1] == 'i':
        #call recursion on string on length-2
        small_string = replace_pi(strings[2:])
        return '3.14' + small_string
    else:
        #call recursion on string on length-1
        small_string = replace_pi(strings[1:])
        return strings[0] + small_string


def take_input():
    strings = input().strip()
    return strings

def main():
    s = take_input()
    result = replace_pi(s)
    print(result)


if __name__ == '__main__':
    main()