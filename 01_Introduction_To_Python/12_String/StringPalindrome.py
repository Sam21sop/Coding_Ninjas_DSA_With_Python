from sys import stdin

def reverse_string(string):
    '''Function will return reverse string.'''
    return string[::-1]


def only_alphanum_string(string):
    '''Function will return only alpha-numeric string.'''
    new_str = ''
    for i in string:
        if i.isalnum():
            new_str += i
    return new_str

    
def is_palindrom(string):
    '''Function will check the string is palindrome or not.'''
    alpha_numeric_string = only_alphanum_string(string)
    rev_str = reverse_string(string)
    if alpha_numeric_string == rev_str:
        return 'true'
    else:
        return 'false'


# Driver Code
if __name__ == '__main__':
    string = input().strip()
    result = is_palindrom(string)
    print(result)