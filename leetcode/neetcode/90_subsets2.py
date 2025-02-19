
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def dfs(index: int, currSet: list):
            if index == len(nums):
                res.append(currSet.copy())
                return
            
            # add nums[i]
            currSet.append(nums[index])
            dfs(index + 1, currSet)
            currSet.pop()

            while index + 1< len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, currSet)
        
        dfs(0, [])
        return res

def test(nums: list):
    sol = Solution()
    print(sol.subsetsWithDup(nums))

if __name__ == '__main__':
    test([1,2,2])