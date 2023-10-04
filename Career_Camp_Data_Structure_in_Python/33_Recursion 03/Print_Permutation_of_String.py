def _permutation_helper(current_permutation, remaining_char):
    if len(remaining_char) == 0:
        print(current_permutation)
        return
    for i in range(len(remaining_char)):
        new_permutation = current_permutation + remaining_char[i]
        new_permutation_char = remaining_char[:i] + remaining_char[i+1:]
        _permutation_helper(new_permutation, new_permutation_char)


def print_permutation(input_string):
    _permutation_helper('', input_string)


def main():
    s = input()
    print_permutation(s)


if __name__ == '__main__':
    main()