from sys import stdin

def reverseEachWord(string):
    words_list = string.split()
    rev_words = [word[::-1] for word in words_list]
    return ' '.join(rev_words)

def main():
    string = stdin.readline().strip()
    result = reverseEachWord(string)
    print(result)

if __name__ == '__main__':
    main()