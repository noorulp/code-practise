
class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


if __name__ == '__main__':

    nums = [1,2,3,1]
    S = Solution()
    print(S.containsDuplicate(nums))