from sys import stdin

def countBracketReversals(expression):
    n = len(expression)

    if n % 2 != 0:      #if the expression length id odd it can't be balanced
        return -1
    
    stack = []
    count = 0

    for char in expression:
        if char == "{":
            stack.append(char)
        elif char == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)
                count += 1
        
    open_brackets_count = 0
    close_brackets_count = 0
    for bracket in stack:
        if bracket == "{":
            open_brackets_count += 1
        elif bracket == "}":
            close_brackets_count += 1
    
    reversal = open_brackets_count // 2 + close_brackets_count // 2

    if open_brackets_count % 2 != 0 or close_brackets_count % 2 != 0:
        reversal += 2
    
    return reversal


def main():
    print(countBracketReversals(stdin.readline().strip()))


if __name__ == '__main__':
    main()