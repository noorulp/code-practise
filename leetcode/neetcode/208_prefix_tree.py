class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for i, char in enumerate(word):
            index = ord(char) - ord('a')
            if ptr.children[index] is None:
                node = TrieNode()
                ptr.children[index] = node
            ptr = ptr.children[index]
           
        ptr.isEndOfWord = True

    def search(self, word: str) -> bool:
        ptr = self.root
        i = 0
        n = len(word)
        while i < n:
            index = ord(word[i]) - ord('a')
            if ptr.children[index] is None:
                return False
            ptr = ptr.children[index]
            i += 1
        if ptr.isEndOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        i = 0
        n = len(prefix)
        while i < n:
            index = ord(prefix[i]) - ord('a')
            if ptr.children[index] is None:
                return False
            ptr = ptr.children[index]
            i += 1
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def test():
    trie = Trie()
    trie.insert('root')
    print(trie.search('root'))
    print(trie.startsWith('rot'))

if __name__ == '__main__':
    test()