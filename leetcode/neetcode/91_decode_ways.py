
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        def getDigit(letter: str):
            # single digit character
            return ord(letter) - ord('0')

        n = len(s)
        res = [0] * n        
        i = 1
        res[0] = 1 # always
        currNum = getDigit(s[0])
        while i < n:
            digit = getDigit(s[i])
            currNum = currNum * 10 + digit
            if digit == 0:
                if (currNum > 20 or getDigit(s[i-1]) == 0):
                    return 0
                else:
                    if i > 1:
                        res[i] = res[i-2]
                    else:
                        res[i] = 1
            else:
                if currNum > 26 or currNum < 10: # currNum < 10 only if prev number was zero     
                    res[i] = res[i-1]
                elif i > 1:
                    res[i] = res[i-1] + res[i-2]
                else:
                    res[i] = res[i-1] + 1
            i += 1
            currNum = digit
        
        return res[-1]

def test(s: str):
    sol = Solution()
    print(sol.numDecodings(s))

if __name__ == '__main__':
    test('2611055971756562') # 