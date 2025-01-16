
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = j = 1
        current = nums[0]
        count = 0
        while j < n:
            if nums[j] == current:
                count += 1
                if count < 2:
                    nums[i] = nums[j]
                    i += 1
            else:
                nums[i] = nums[j]
                current = nums[i]
                i += 1
                count = 0
            j += 1
        return i  

    def removeDuplicates2(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1

        return i    


if __name__ == '__main__':
    nums = [0,0,1,1,1,1,2,3,3]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print(k)
    print(nums)