def reverse_stack(populated_stack, empty_stack):
    while len(populated_stack) != 0:
        peek_element = populated_stack.pop()
        empty_stack.append(peek_element)
    return empty_stack

def take_input():
    size = int(input())
    if size == 0:
        return list(), 0
    input_stack = list(map(int, input().strip().split()))
    return input_stack


def main():
    input_stack = take_input()
    rev_stack = reverse_stack(input_stack, [])
    print(*rev_stack)

if __name__ == '__main__':
    main()