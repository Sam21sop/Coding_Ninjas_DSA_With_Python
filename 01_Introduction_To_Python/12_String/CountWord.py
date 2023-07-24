from sys import stdin


def countWords(string):
    word_list = string.split()
    count_word = len(word_list)
    return count_word



if __name__ == "__main__":
    string = stdin.readline().strip()
    result = countWords(string)
    print(result)