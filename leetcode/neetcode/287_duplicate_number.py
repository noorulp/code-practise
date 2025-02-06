class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        # find cycle
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        ptr = 0
        # find cycle beginning
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]
        
        return ptr

if __name__ == '__main__':
    nums = [1,3,3,2]
    sol = Solution()
    print(sol.findDuplicate(nums))