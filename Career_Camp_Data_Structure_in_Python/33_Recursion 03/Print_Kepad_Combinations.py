keypad = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz' } 

def generate_substring(digits_string, current_string, index, result):
    if len(digits_string) == index:
        print(current_string)
        return
    digit = digits_string[index]
    charactor = keypad[digit]
    for char in charactor:
        generate_substring(digits_string, current_string+char, index+1, result)


def main():
    n = input()
    result = []
    generate_substring(n, '', 0, result)


if __name__ == '__main__':
    main()