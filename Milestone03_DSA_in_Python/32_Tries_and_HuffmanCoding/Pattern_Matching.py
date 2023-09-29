'''
Time complexity: O(n * m)   
Space complexity:O(n * m)
where n is number of word in trie and m is average length of word
'''

from sys import stdin 

class TrieNode:
    count = 0
    def __init__(self, char='\0') -> None:
        self.char = char
        self.terminal = False
        self.children = {}
        TrieNode.count += 1


class Trie:
    def __init__(self) -> None:
        self.__root = TrieNode()

    def insert(self, word):
        curr = self.__root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
        curr.terminal = True

    def search(self, word):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True
    
    def pattern_matching(self, vect, pattern):
        for word in vect:
            word_length = len(word)
            for j in range(0, word_length):
                self.insert(word[j:])
        return self.search(pattern)
    
    def display(self):
        curr = self.__root
        for char in curr.children:
            self.__display(curr.children[char], '')

    def __display(self, root, word):
        new_word = word + root.char
        if root.terminal:
            print(new_word)
        for char in root.children:
            self.__display(root.children[char], new_word)


def take_input():
    n = int(input())
    if n == 0:
        return list(), 0
    li = list(map(str, stdin.readline().strip().split()))
    pattern = stdin.readline().rstrip()
    return li, n, pattern


def main():
    lst_of_word, n, pattern = take_input()
    t = Trie()
    if t.pattern_matching(lst_of_word, pattern):
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()


# 4
# abc def ghi hg
# hi
# true

# 4
# abc def ghi cba
# de
# false