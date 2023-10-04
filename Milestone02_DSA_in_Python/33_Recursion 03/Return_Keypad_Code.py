keypad = {
        '2': 'abc', 
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl', 
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz' }

def generate_combinations(digits, index, current_string, result):
        if index == len(digits):
            if current_string:
                result.append(current_string)
            return
        
        current_digit = digits[index]
        characters = keypad[current_digit]
        
        for char in characters:
            generate_combinations(digits, index + 1, current_string + char, result)

def get_keypad_combinations(n):
    if n == 0 or n == 1:
        return []
    digits = str(n)
    result = []
    generate_combinations(digits, 0, "", result)
    return result

def main():
    n = int(input())
    output = get_keypad_combinations(n)

    # Output
    for string in output:
        print(string)


if __name__ == "__main__":
    main()