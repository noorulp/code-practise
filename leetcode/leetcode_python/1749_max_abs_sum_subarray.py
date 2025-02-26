
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxSum = 0
        minSum = 0
        sum = 0
        nsum = 0
        for num in nums:
            if num >= 0:
                sum += num
                maxSum = max(maxSum, sum)
                minSum = min(minSum, nsum + num)
                nsum = min(0, nsum + num)
            else:
                maxSum = max(maxSum, sum + num)
                sum = max(0, sum + num)
                nsum += num
                minSum = min(minSum, nsum)

        return(max(maxSum, abs(minSum)))

def test(nums: list):
    sol = Solution()
    print(sol.maxAbsoluteSum(nums))

if __name__ == '__main__':
    test(nums = [2,-5,4,-1,3,-2])
    test(nums = [1,-3,2,3,-4])