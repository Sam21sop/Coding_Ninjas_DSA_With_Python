def even_odd(number):
    '''Function return is even or odd'''
    if number % 2 == 0:
        return 'Number is even.'
    else:
        return 'Number is odd.'


if __name__ == "__main__":
    num = int(input())
    result = even_odd(num)
    print(result)
