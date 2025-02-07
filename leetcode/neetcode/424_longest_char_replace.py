class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict()
        maxlen = 0
        l = 0
        for i, char in enumerate(s):
            counts[char] = 1 + counts.get(char, 0)

            while i - l + 1 - max(counts.values()) > k:
                counts[s[l]] = counts[s[l]] - 1
                l += 1
            if i - l + 1 > maxlen:
                maxlen = i - l + 1

        return maxlen

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
    