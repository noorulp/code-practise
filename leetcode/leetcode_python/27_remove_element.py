
class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:
        i = j = 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i + 1

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    k = sol.removeElement(nums, val)
    print(k)
    print(nums)