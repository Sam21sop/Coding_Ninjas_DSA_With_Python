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
    

    def _delete_helper(self, node, word, index):
        if index == len(word):
            if node.is_terminal:
                node.is_terminal = False
                return True
            return False
        
        char = word[index]
        if char not in node.children:
            return False
        
        can_delete = self._delete_helper(node.children[char], word, index+1)
        if can_delete:
            del node.children[char]
            return not node.is_terminal and len(node.children) == 0
        return False


    def delete(self, word):
        self._delete_helper(self.root, word, 0)


def main():
    trie = Tries()

    # adding word in tries
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    # searhinf word in tries
    print(trie.search("apple"))  
    print(trie.search("appapp"))    

    # word start with
    print(trie.starts_with("ban"))  
    print(trie.starts_with("ora"))

    # delete word in tries
    trie.delete("apple")
    print(trie.search("apple"))    


if __name__ == '__main__':
    main()