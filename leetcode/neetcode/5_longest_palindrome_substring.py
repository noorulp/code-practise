
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        resIndex = 0
        resLen = 0
        n = len(s)
        for i in range(0, n):
            # even
            l = i - 1
            r = i
            while l >=0 and r < n:
                if s[l] != s[r]:
                    break
                if r - l + 1 > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            # odd
            l = i - 1
            r = i + 1
            while l >=0 and r < n:
                if s[l] != s[r]:
                    break
                if r - l + 1 > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        if resLen == 0:
            return s[0]

        return s[resIndex: resIndex + resLen]

def test(s: str):
    sol = Solution()
    print(sol.longestPalindrome(s))


if __name__ == '__main__':
    test('ab')