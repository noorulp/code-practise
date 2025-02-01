class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashDict = dict()
        for i, num in enumerate(nums):
            index = hashDict.get(target-num, -1)
            if index != -1:
                return [i, index]
            hashDict[num] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    S = Solution()
    print(S.twoSum(nums, target))