def remove_duplicates(string):
    '''Function will remove all duplicates char from string'''
    new_string = ''
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string


def is_present(user_string, keyboard_string):
    '''Function retrun True if word present in the given string otherwise False.'''
    new_string = remove_duplicates(keyboard_string)
    flag = True
    if len(new_string) == len(user_string):
        for char in user_string:
            if char not in new_string:
                flag = False
                break
    return flag

def take_input():
    '''function will take user input'''
    user_input = input()
    key_generated = input()
    return user_input, key_generated


def main():
    t = int(input())
    while t > 0:
        user_input, keyboard_generated = take_input()
        result = is_present(user_input, keyboard_generated)
        if result:
            print('true')
        else:
            print('false')
        t -= 1


if __name__ == '__main__':
    main()