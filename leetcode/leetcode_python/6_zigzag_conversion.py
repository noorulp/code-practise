class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        i = 0
        while i < numRows:
            jump1 = (numRows - i - 1) * 2
            jump2 = (i * 2)
            if jump1 == 0:
                jump1 = jump2
            if jump2 == 0:
                jump2 = jump1
            start = i
            while start < len(s):
                res += s[start]
                start += jump1
                if start < len(s):
                    res += s[start]
                    start += jump2
            i += 1
        return res

def test(s: str, numRows: int, output: str):
    sol = Solution()
    res = sol.convert(s, numRows)
    assert res == output

if __name__ == '__main__':
    test(s = "A", numRows= 2, output= "A")
    test(s = "PAYPALISHIRING", numRows = 3, output= "PAHNAPLSIIGYIR")
    test(s = "PAYPALISHIRING", numRows = 4, output= "PINALSIGYAHRPI")