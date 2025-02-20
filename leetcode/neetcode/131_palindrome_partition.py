
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        def checkPalindrome(word: str) -> bool:
            i = 0
            j = len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []
        def dfs(palindromes: list, word: str):
            n = len(word)
            if checkPalindrome(word):
                palindromes.append(word)
                res.append(palindromes.copy())
                palindromes.pop()

            for i in range(1, n):
                part = word[0:i]
                if checkPalindrome(part):
                    palindromes.append(part)
                    dfs(palindromes, word[i:n])
                    palindromes.pop()
                

        dfs([], s)
        return res

def test(s: str):
    sol = Solution()
    print(sol.partition(s))

if __name__ == '__main__':
    test('aba')