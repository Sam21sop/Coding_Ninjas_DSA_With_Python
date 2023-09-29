class TriesNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_terminal = False



class Tries:
    def __init__(self) -> None:
        self.root = TriesNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TriesNode()
            node = node.children[char]
        node.is_terminal = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_terminal
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    

def main():
    trie = Tries()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    print(trie.search("apple"))  
    print(trie.search("app"))    
    print(trie.search("banana")) 
    print(trie.search("orange")) 
    print(trie.starts_with("ban"))  
    print(trie.starts_with("ora"))  


if __name__ == '__main__':
    main()