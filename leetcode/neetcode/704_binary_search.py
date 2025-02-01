class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((right + left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    sol = Solution()
    print(sol.search(nums, target))
