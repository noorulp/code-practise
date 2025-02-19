
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def getSubsets(currSet: list, index: int):
            if index == len(nums):
               res.append(currSet.copy())
               return
            # don't add nums[index]
            getSubsets(currSet.copy(), index + 1)
            currSet.append(nums[index])
            getSubsets(currSet.copy(), index + 1)

        getSubsets([], 0)
        return res

def test(nums: list):
    sol = Solution()
    print(sol.subsets(nums))


if __name__ == '__main__':
    test([1,2,3])
    test([0])