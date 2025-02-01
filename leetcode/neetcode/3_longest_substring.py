class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = dict()
        l = 0
        r = 0
        maxLen = 0
        for i, char in enumerate(s):
            index = charMap.get(char, -1)
            charMap[char] = i
            if index > -1 and l <= index:
                l = index + 1
            r += 1
            if r - l > maxLen:
                maxLen = r - l
        return maxLen


if __name__ == '__main__':
    sol = Solution()
    s = "abba"
    print(sol.lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(sol.lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))