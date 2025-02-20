
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.index = -1

    def addWord(self, word: str, index: int):
        node = self
        for char in word:
            i = ord(char) - ord('a')
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isEndOfWord = True
        node.index = index

class Solution:
    def findWord(self, board: list[list[str]], words: list[str]) -> list[str]:
        # add words
        root = TrieNode()
        for i, word in enumerate(words):
            root.addWord(word, i)

        ROW = len(board)
        COL = len(board[0])
        res = []

        def dfs(i: int, j: int, node: TrieNode):
            if i < 0 or j < 0 or i == ROW or j == COL or board[i][j] is None:
                return
            if node.children[ord(board[i][j]) - ord('a')] is None:
                return
            
            prev = node
            node = node.children[ord(board[i][j]) - ord('a')]
            prevLetter = board[i][j]
            board[i][j] = None
            if node.isEndOfWord and node.index != -1:
                res.append(words[node.index])
                node.index = -1

            dfs(i - 1, j, node) # up
            dfs(i + 1, j, node) # down
            dfs(i, j - 1, node) # left
            dfs(i, j + 1, node) # right

            board[i][j] = prevLetter
            node = prev
            

    
        for i in range(0, ROW):
            for j in range(0, COL):
                dfs(i, j, root)
                if len(res) == len(words):
                    break
        return res



def test(board: list[list[str]], words: list[str]):
    sol = Solution()
    print(sol.findWord(board, words))


if __name__ == '__main__':
    test(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","oat","eat","rain"])