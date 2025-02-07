class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nt = len(t)
        hashT = dict()
        for char in t:
            hashT[char] = 1 + hashT.get(char, 0)
        left = 0
        ns = len(s)
        right = 0
        while hashT.get(s[left], 0) == 0:
            left += 1
            if left == ns:
                return ""
        right = left
        hashS = dict()
        n = 0
        minSubLen = float('inf')
        minWin = None
    
        while right < ns:
            freq = hashT.get(s[right], 0)
            if freq > 0:
                # char in string t
                hashS[ s[right] ] = 1 + hashS.get(s[right], 0)
                if hashS[ s[right] ] <= hashT[ s[right] ]:
                    n += 1
                else:
                    # extra chars
                    while hashS.get(s[left], 0)  > hashT.get(s[left], -1):
                        cnt = hashS.get(s[left], 0)
                        if cnt > 0:
                            hashS[ s[left] ] = hashS[ s[left] ] - 1
                        left += 1
                if n == nt:
                        # found string t
                        subLen = right - left + 1
                        if subLen < minSubLen:
                            minSubLen = subLen
                            minWin = (left, right)
            right += 1
        
        if minWin:
            return s[minWin[0]:minWin[1] + 1]
        return ""


if __name__ == '__main__':
    sol = Solution()
    t = ""
    s = ""
    print(sol.minWindow(s, t))