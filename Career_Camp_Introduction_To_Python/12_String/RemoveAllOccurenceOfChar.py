from sys import stdin

def removeAllOccurrencesOfChar(string, ch):
    return string.replace(ch, '')


def main():
    string = stdin.readline().strip()
    ch = stdin.readline().strip()
    result = removeAllOccurrencesOfChar(string, ch)
    print(result)

if __name__ == '__main__':
    main()