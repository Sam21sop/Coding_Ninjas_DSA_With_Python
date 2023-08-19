def check_ab(string):
    if len(string) == 0:
        return True
    if string[0] == 'a':
        if len(string[1:]) > 0 and string[1:3] == 'bb':
            return check_ab(string[3:])
        else:
            return check_ab(string[1:])
    else:
        return False
    

def main():
    s = input()
    result = check_ab(s)
    if result:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()    