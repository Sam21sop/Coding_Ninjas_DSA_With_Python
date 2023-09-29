from sys import stdin 

class TrieNode:
    def __init__(self, char='\0') -> None:
        self.char = char
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.__root = TrieNode()
        self.num_word = 0


    def insert(self, word):
        curr = self.__root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
        curr.terminal = True
        self.num_word += 1


    def search(self, word):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True



    def printS(self, root, s):
        if root == None:
            return
        if root.terminal:
            print(s)

        for char in root.children:
            t = s + char
            self.printS(root.children[char], t)

    
    def auto_complete_helper(self, root, pattern, output):
        if root == None:
            return 
        if len(pattern) == 0:
            if root.terminal:
                print(output)

            for char in root.children:
                s = output + char
                self.printS(root.children[char], s)
            return
        index_char =  pattern[0]
        output += pattern[0]
        if root.children.get(index_char) != None:
            self.auto_complete_helper(root.children[index_char], pattern[1:], output)


    def auto_complete(self, input_s, pattern):
        for i in range(len(input_s)):
            self.insert(input_s[i])
        output = ""
        self.auto_complete_helper(self.__root, pattern, output)



def main():
    t = Trie()
    n = int(stdin.readline().strip())
    words = stdin.readline().strip().split()
    pattern = stdin.readline().strip()
    t.auto_complete(words, pattern)


if __name__ == '__main__':
    main()
