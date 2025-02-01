class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        output = [1] * l
        i = 0
        lprod = 1
        rprod = 1
        while i < l:
            output[i] *= lprod
            output[l-i-1] *= rprod
            lprod *= nums[i]
            rprod *= nums[l-i-1]
            i += 1
        return output


if __name__ == '__main__':
    S = Solution()
    nums = [2,3,5,7]
    nums1 = [-1,9]
    print(S.productExceptSelf(nums))
    print(S.productExceptSelf(nums1))