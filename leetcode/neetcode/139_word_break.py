
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
    
    def add(self, word: str):
        node = self
        for letter in word:
            index = ord(letter) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True
    
    def match(self, string: str) -> False:
        node = self
        for letter in string:
            index = ord(letter) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.isEndOfWord

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        maxLen = len(wordDict[0])
        root = TrieNode()
        for word in wordDict:
            maxLen = max(maxLen, len(word))
            root.add(word)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n, -1, -1):
            minI = min(n, i + maxLen)
            for j in range(i, minI):
                if root.match(s[i:j + 1]):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]


def test(s: str, wordDict: list):
    sol = Solution()
    print(sol.wordBreak(s, wordDict))


if __name__ == '__main__':
    test(s = 'comecode', wordDict= ['come', 'code', 'ode'])
    test(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
         wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])