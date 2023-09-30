from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class TrieNode:
    def __init__(self, char='\0') -> None:
        self.char = char
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.__root = TrieNode()


    def insert(self, word):
        curr_root = self.__root
        for i in range(len(word)):
            if word[i] in curr_root.children:
                curr_root = curr_root.children.get(word[i])
            else:
                new_node = TrieNode(word[i])
                curr_root.children[word[i]] = new_node
                curr_root = new_node
        curr_root.terminal = True


    def search(self, word):
        curr_root = self.__root
        for i in range(len(word)):
            if word[i] in curr_root.children:
                curr_root = curr_root.children.get(word[i])
            else:
                return False
        return curr_root.terminal == True
    

    def _delete_helper(self, root, word):
        if len(word) == 0:
            root.terminal = False
            return 
        curr_char = word[0]
        child_node = root.children.get(curr_char)
        if child_node is not None:
            self._delete_helper(child_node, word[1:])
            if child_node.terminal is False and len(child_node.children) == 0:
                root.children.pop(curr_char)
        return
    

    def delete(self, word):
        self._delete_helper(self.__root, word)

    
    def __print_helper(self, root, word):
        if root is None:
            return
        if root.terminal:
            print(word)
        for child in root.children:
            child_node = root.children.get(child)
            temp = word + child
            self.__print_helper(child_node, temp)

    def display(self):
        curr_trie = self.__root
        self.__print_helper(curr_trie, '')

    
    def isPalindromPair(self, word):
        for w in word:
            self.insert(self.reversedWord(w))
        return self.isPalindromPairHelper(self.__root, word)


    def reversedWord(self, word):
        return word[::-1]
    
    def isPalindromPairHelper(self, root, words):
        for word in words:
            if self.doesPairExist(root, word, 0):
                return True
        return False
    
    def doesPairExist(self, root, word, startIndex):
        if word == '':
            return True
        if startIndex == len(word):
            if root.terminal:
                return True
            return self.checkRemainingBranches(root, "")
        corresponding_child = root.children.get(word[startIndex])
        if corresponding_child is None:
            if root.terminal:
                return self.checkWordForPalindrom(word[startIndex:])
            return False
        return self.doesPairExist(corresponding_child, word, startIndex+1)
    
    
    def checkRemainingBranches(self, root, word):
        if root.terminal:
            if self.checkWordForPalindrom(word):
                return True
        for child in root.children:
            child_node = root.children.get(child)
            temp = temp + child
            if self.checkRemainingBranches(child_node, temp):
                return True
        return False
    

    def checkWordForPalindrom(self, word):
        for i in range(len(word) // 2):
            if word[i] != word[-1-i]:
                return False
        return True
    

def take_input():
    n = int(input())
    if n == 0:
        return list(), 0
    return list(map(str, input().strip().split())), 0


def main():
    word_lst , n = take_input()
    t = Trie()
    if t.isPalindromPair(word_lst):
        print('true')
    else:
        print('false')


if __name__ == "__main__":
    main()


# 4
# abc def ghi cba


# 2
# abc def