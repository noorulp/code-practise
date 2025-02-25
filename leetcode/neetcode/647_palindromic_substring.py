
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(0, n):
            # even
            l = i
            r = i + 1
            while l >=0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # odd
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
    

def test(s: str):
    sol = Solution()
    print(sol.countSubstrings(s))


if __name__ == '__main__':
    test('abc')
    test('abba')
    test('aaa')