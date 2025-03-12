
class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        ''' returns index closest to the number
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if ( mid == 0 or nums[mid - 1] < target ) and nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return mid

    def maxmimumCount(self, nums: list[int]) -> int:
        ni = self.binarySearch(nums, 0)
        if nums[ni] > -1:
            ni -= 1
        pi = self.binarySearch(nums, 1)
        if nums[pi] < 1:
            pi += 1
        return max(ni + 1, len(nums) - pi)

def test(nums: list[int]):
    sol = Solution()
    print(sol.maxmimumCount(nums))

if __name__ == '__main__':
    nums = [-3,-2,0,0,0,4,5,6,10]
    test(nums)