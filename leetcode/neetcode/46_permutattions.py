
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        indices = [0] * len(nums)

        def dfs(indices: list, currSet: list):
            n = len(nums)
            if len(currSet) == n:
                res.append(currSet.copy())
                return

            for i in range(0, n):
                if indices[i] == 0:
                    indices[i] = 1
                    currSet.append(nums[i])
                    dfs(indices, currSet)
                    indices[i] = 0
                    currSet.pop()
                
        dfs(indices, [])
        return res


def test(nums: list):
    sol = Solution()
    print(sol.permute(nums))

if __name__ == '__main__':
    test([1,2])
