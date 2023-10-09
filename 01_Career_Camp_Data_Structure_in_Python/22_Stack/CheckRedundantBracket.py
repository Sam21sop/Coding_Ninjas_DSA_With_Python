from sys import stdin

def check_redundant_bracket(expression):
    stack = []
    for char in expression:
        if char == ')':
            top = stack[-1]
            stack.pop()
            is_redundant = True
            while top != '(':
                if top in ["+", '-', '*', '/']:
                    is_redundant = False
                top = stack[-1]
                stack.pop()
            if is_redundant:
                return True
        else:
            stack.append(char)
    return False


def main():
    expression = stdin.readline().strip()
    if check_redundant_bracket(expression):
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()