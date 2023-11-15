def remove_backspaces(input_string: str):
    stack = []
    for char in input_string:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)


def main():
    input_str = input()
    res = remove_backspaces(input_str)
    print(res)


if __name__ == '__main__':
    main()