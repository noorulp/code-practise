
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        majority = nums[0]
        n = len(nums)
        for num in nums:
            if num == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    majority = num
        return majority


if __name__ == '__main__':
    nums = [2,2,1,1,4,2]
    sol = Solution()
    k = sol.majorityElement(nums)
    print(k)
