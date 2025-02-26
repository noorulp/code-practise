
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        product = 1
        maxProduct = float('-inf')
        lastNegativeNum = 0
        for num in nums:
            if num > -1:
                product *= num
                if product > maxProduct:
                    maxProduct = product
                if num == 0:
                    product = 1
                    lastNegativeNum = 0
            else:
                if lastNegativeNum == 0:
                    lastNegativeNum = num * product
                    if num > maxProduct:
                        maxProduct = num
                    product = 1
                else:
                    product = product * lastNegativeNum * num
                    lastNegativeNum = 0
                    if product > maxProduct:
                        maxProduct = product
        product = 1
        lastNegativeNum = 0
        for i in range(len(nums) - 1, 0, -1):
            num = nums[i]
            if num > -1:
                product *= num
                if product > maxProduct:
                    maxProduct = product
                if num == 0:
                    product = 1
                    lastNegativeNum = 0
            else:
                if lastNegativeNum == 0:
                    lastNegativeNum = num * product
                    if num > maxProduct:
                        maxProduct = num
                    product = 1
                else:
                    product = product * lastNegativeNum * num
                    lastNegativeNum = 0
                    if product > maxProduct:
                        maxProduct = product
        return maxProduct

def test(nums: list):
    sol = Solution()
    print(sol.maxProduct(nums))


if __name__ == '__main__':
    test([2,-5,-2,-4,3])