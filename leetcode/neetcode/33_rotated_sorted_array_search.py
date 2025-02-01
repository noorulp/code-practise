class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left  + right) // 2
            if nums[mid-1] > nums[mid]:
                break
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        offset = mid
        left = 0
        right = len(nums) - 1
        n = len(nums)
        while left <= right:
            mid = (left + right) // 2
            num = nums[(offset + mid) % n]
            if  num == target:
                return (offset + mid) % n
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            
if __name__ == '__main__':
    sol = Solution()
    nums = [5,1,3]
    target = 1
    print(sol.search(nums, target))
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(sol.search(nums, target))
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(sol.search(nums, target))
    nums = [1]
    target = 0
    print(sol.search(nums, target))
