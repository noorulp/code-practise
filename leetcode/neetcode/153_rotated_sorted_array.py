class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = (left  + right)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        mid = (left + right)//2
        return nums[mid]

if __name__ == '__main__':
    sol = Solution()
    nums = [3,4,5,1,2]
    print(sol.findMin(nums))
    nums = [4,5,6,7,0,1,2]
    print(sol.findMin(nums))
    nums = [11,13,15,17]
    print(sol.findMin(nums))