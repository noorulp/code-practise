class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict()
        l = 0
        maxf = 0
        for i, char in enumerate(s):
            counts[char] = 1 + counts.get(char, 0)
            maxf = max(counts[char], maxf)
            
            lenSub = i - l + 1
            while lenSub - counts[char] > k:
                




if __name__ == '__main__':
    sol = Solution()
    s = "BAAA"
    k = 0
    print(sol.characterReplacement(s, k))
    s = "ABAB"
    k = 0
    print(sol.characterReplacement(s, k))
    s = "ADEABCB"
    k = 1
    print(sol.characterReplacement(s, k))
    s = "ABABACD"
    k = 2
    print(sol.characterReplacement(s, k))
    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s, k))
    