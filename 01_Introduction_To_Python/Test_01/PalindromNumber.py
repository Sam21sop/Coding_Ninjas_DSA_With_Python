def rev_num(number):
    ''' Return the reverse number.'''
    rev = 0
    while number != 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10
    return rev 


def is_palindrom(number):
    ''' Check whether number is palindrom or not.'''
    reversed_number = rev_num(number)
    # print(reversed_number)
    if number == reversed_number:
        return 'true'
    else:
        return 'false'


if __name__ == "__main__":
    num = int(input())
    RES = is_palindrom(num)
    print(RES)