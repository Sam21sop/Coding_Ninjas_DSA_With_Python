from sys import stdin
from collections import Counter


def highestOccuringChar(string):
    if not string:
        return ''
    frequency_count = Counter(string)
    max_occurence = max(frequency_count.values())
    for char, count in frequency_count.items():
        if count == max_occurence:
            max_ocurred_char = char
    return max_ocurred_char


def main():
    string = stdin.readline().strip()
    result = highestOccuringChar(string)
    print(result)


if __name__ == '__main__':
    main()