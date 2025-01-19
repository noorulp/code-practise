class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    S = Solution()
    s = "A man, a plan, a canal: Panama"
    print(S.isPalindrome(s))
    s = "race a car"
    print(S.isPalindrome(s))
    s = " "
    print(S.isPalindrome(s))