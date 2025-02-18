class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if ptr.children[index] is None:
                ptr.children[index] = TrieNode()
            ptr = ptr.children[index]
        ptr.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def wordMatch(node: TrieNode, start: int) -> bool:
            if start == len(word):
                return node.isEndOfWord
            
            isValid = False
            if word[start] == '.':
                for child in node.children:
                    if child:
                        isValid = wordMatch(child, start + 1)
                        if isValid:
                            return True
            else:
                index = ord(word[start]) - ord('a')
                if node.children[index] is not None:
                    return wordMatch(node.children[index], start + 1)
            
            return False
        
        found = wordMatch(self.root, 0)
        return found


def test(funcs: list, vals: list):
    word = WordDictionary()
    i = 1
    while i < len(vals):
        f = funcs[i]
        v = vals[i]
        if f == 'addWord':
            word.addWord(v[0])
        else:
            print(word.search(v[0]))
        i += 1

if __name__ == '__main__':
    test(["WordDictionary","addWord","addWord","addWord","search","search","search","search"], 
         [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]])