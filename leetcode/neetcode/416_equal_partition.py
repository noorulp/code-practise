class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        n = len(nums)
        memo = [[False for _ in range(0, target + 1)] for _ in range(0, n)]
        memo[0][0] = True
        if nums[0] < target + 1:
            memo[0][nums[0]] = True

        for i in range(1, n):
            memo[i][0] = True
            for j in range(0, target + 1):
                if memo[i - 1][j]:
                    memo[i][j] = True
                if j > nums[i] and memo[i - 1][j - nums[i]] is True:
                    memo[i][j] = True
            if memo[i][target] is True:
                return True

        return False

def test(nums: list):
    sol = Solution()
    print(sol.canPartition(nums))

if __name__ == '__main__':
    test(nums = [14,9,8,4,3,2])