class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max = 0
        while len(num_set) > 0:
            temp = 0
            num = num_set.pop()
            i = 1
            while num + i in num_set:
                num_set.discard(num + i)
                i += 1
            j = 1
            while num - j in num_set:
                num_set.discard(num - j)
                j += 1
            temp = i + j - 1
            if temp > max:
                max = temp
        return max



if __name__ == '__main__':
    S = Solution()
    nums = [100,4,200,1,3,2]
    print(S.longestConsecutive(nums))
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(S.longestConsecutive(nums))