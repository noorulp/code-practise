class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if nums[left] > target:
            return 0
        if nums[right] < target:
            return n
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if target < nums[mid]:
            return mid 
        return mid + 1

if __name__ == '__main__':
    nums = [1,3,5,7,9,10,12,30]
    target = 15
    sol = Solution()
    print(sol.searchInsert(nums, target))