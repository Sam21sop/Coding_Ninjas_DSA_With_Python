from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class TriesNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TriesNode()
        self.word_count = 0                         # initialize word count to 0

    
    def insertWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TriesNode()
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.word_count += 1


    def _remove_helper(self, node, word, index):
        if len(word) == index:
            if node.is_end_of_word:
                node.is_end_of_word = False
                self. word_count -= 1
                return True
            return False
        
        char = word[index]
        if char not in node.children:
            return False
        
        can_remove = self._remove_helper(node.children[char], word, index + 1)
        if can_remove:
            if not node.children[char].is_end_of_word and not node.children[char].children:
                del node.children[char]
            return not node.is_end_of_word and node.children
        return False


    def removeWord(self, word):
        self._remove_helper(self.root, word, 0)


    def countWords(self):
        return self.word_count


def main():
    t = Trie()
    inputs = stdin.readline().strip().split( )
    choice = int(inputs[0])

    if len(inputs) != 1:
        word = inputs[1]

    while choice != -1:
        if choice==1:
            t.insertWord(word)
        if choice==2:
            t.removeWord(word)
        if choice==3:
            print(t.countWords())
        inputs = stdin.readline().strip().split( )
        choice = int(inputs[0])
        if len(inputs)!=1:
            word = inputs[1]

if __name__ == '__main__':
    main()


# 1 a
# 1 ab
# 1 abcd
# 3
# 2 abcd
# 2 abcd
# 3
# -1