def max_number(number):
    '''Function return Max Number'''
    digits = str(number)
    max_num = 0
    for i in range(len(digits)):
        new_digits = digits[:i] + digits[i+1:]
        new_number = int(''.join(new_digits))
        max_num = max(new_number, max_num)
    return max_num



if __name__ == "__main__":
    num = int(input())
    result = max_number(num)
    print(result)
