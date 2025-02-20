
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        res = []
        numpad  = dict()
        numpad['2'] = ['a','b','c']
        numpad['3'] = ['d','e','f']
        numpad['4'] = ['g','h','i']
        numpad['5'] = ['j','k','l']
        numpad['6'] = ['m','n','o']
        numpad['7'] = ['p','q','r','s']
        numpad['8'] = ['t','u','v']
        numpad['9'] = ['w','x','y','z']

        def permute(index: int, cur: str):
            if index == len(digits):
                res.append(cur)
                return
            
            for letter in numpad[digits[index]]:
                permute(index + 1, cur + letter)
        
        permute(0, '')
        return res

def test(digits: str):
    sol = Solution()
    print(sol.letterCombinations(digits))

if __name__ == '__main__':
    test("23")
    test("")
    test("27")