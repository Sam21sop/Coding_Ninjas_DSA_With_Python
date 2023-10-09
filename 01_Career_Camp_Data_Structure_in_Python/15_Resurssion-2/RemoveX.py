def remove_x(strings):
    if len(strings) == 0:
        return strings
    if strings[0] == 'x':
        return remove_x(strings[1:])
    else:
        return strings[0] + remove_x(strings[1:])
    

def take_input():
    strings = input().strip()
    return strings


def main():
    s = take_input()
    result = remove_x(s)
    print(result)

if __name__ == '__main__':
    main()