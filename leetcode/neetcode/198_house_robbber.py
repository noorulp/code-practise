
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[0] + nums[2], nums[1])
        
        money = [0] * 3
        money[0] = nums[0]
        money[1] = nums[1]
        money[2] = nums[2] + nums[0]
        i = 3
        while i < n:
            money_n = max(money[0], money[1]) + nums[i]
            money[0] = money[1]
            money[1] = money[2]
            money[2] = money_n
            i += 1
        
        return max(money[1], money[2])

def test(nums):
    sol = Solution()
    print(sol.rob(nums))

if __name__ == '__main__':
    test([6,1,2,9,2,1,3,3])
