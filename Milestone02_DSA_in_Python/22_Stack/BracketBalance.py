from sys import stdin

def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0


def main():
    expres = stdin.readline().strip()
    if is_balanced(expres):
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()