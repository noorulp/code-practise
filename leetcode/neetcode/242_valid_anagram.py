class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashArr = [0] * 26
        for i,j in zip(s,t):
            hashArr[ord(i)-97] += 1
            hashArr[ord(j)-97] -= 1
        
        for num in hashArr:
            if num != 0:
                return False
        
        return True

if __name__ == '__main__':
    s = "hello"
    t = "olehh"
    S = Solution()
    print(S.isAnagram(s,t))