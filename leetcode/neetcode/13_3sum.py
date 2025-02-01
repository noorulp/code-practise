class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        target = 0
        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if num + nums[l] + nums[r] < target:
                    l += 1
                elif num + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return output


if __name__ == '__main__':
    S = Solution()
    nums = [-1,0,1,2,-1,-4,2,2]
    print(S.threeSum(nums))
    nums = [0,1,1]
    print(S.threeSum(nums))
    nums = [0,0,0]
    print(S.threeSum(nums))
    nums = [-2,0,0,2,2]
    print(S.threeSum(nums))