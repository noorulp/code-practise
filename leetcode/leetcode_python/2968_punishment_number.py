import math

class Solution: 
    def punishmentNumber(self, n: int) -> int:
        punish = 1
        for i in range(2, n + 1):
            sq = i * i
            if self.checkDigitSum(sq, i):
                punish += sq
        return punish

    def checkDigitSum(self, num: int, target: int) -> bool:
        
        def check(n: int, target: int) -> bool:
            if n == 0:
                return target == 0
            
            r = math.floor(math.log10(n))
            pow10 = 10 ** r
            while pow10:
                left = int( n / pow10)
                remainder = n % pow10
                if left <= target:
                    isValid = check(remainder, target - left)
                    if isValid:
                        return True
                pow10 = int(pow10 / 10)
            
            return False
        
        b = check(num, target)
        return b

def test(n: int):
    sol = Solution()
    print(sol.punishmentNumber(n))

if __name__ == '__main__':
    test(37)