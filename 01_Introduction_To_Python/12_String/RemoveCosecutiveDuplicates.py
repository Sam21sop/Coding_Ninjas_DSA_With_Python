from sys import stdin

def removeConsecutiveDuplicates(string):
    if len(string) == 0:
        return ''

    new_string = string + ' '
    result = ''
    for i in range(1, len(new_string) - 1):
        if new_string[i+1] != new_string[i]:
            result += new_string[i]
    return result

def main():
    new_string = stdin.readline().strip()
    result = removeConsecutiveDuplicates(new_string)
    print(result)

if __name__ == '__main__':
    main()