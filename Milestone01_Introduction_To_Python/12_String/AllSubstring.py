from sys import stdin

def all_substring(string):
    n = len(string)
    for i in range(n):
        for j in range(i+1, n+1):
            print(string[i:j])


if __name__ == '__main__':
    string = stdin.readline().strip()
    all_substring(string)
