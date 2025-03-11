from collections import deque

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        i = len(nums) - 1
        i -= 1
        maxLIS = 1
        while i >= 0:
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            maxLIS = max(maxLIS, dp[i])
            i -= 1
        
        return maxLIS


def test(nums: list):
    sol = Solution()
    print(sol.lengthOfLIS(nums))

if __name__ == '__main__':
    test([1,3,6,7,9,4,10,5,6])