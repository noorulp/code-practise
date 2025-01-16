
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = 1
        j = 1
        current = nums[0]
        while j < n:
            if nums[j] != current:
                current = nums[j]
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
    

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print(k)
    print(nums)
