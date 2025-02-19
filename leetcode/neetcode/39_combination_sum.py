
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        combination = []
        res = []

        def dfs(startIndex: int, currSum: int):
            if currSum == target:
                res.append(combination.copy())
                return

            n = len(candidates)
            for i in range(startIndex, n):
                num = candidates[i]
                if currSum + num > target:
                    return
                combination.append(num)
                dfs(i, currSum + num)
                combination.pop()
        
        dfs(0, 0)
        return res

def test(candidates: list[int], target: int):
    sol = Solution()
    print(sol.combinationSum(candidates, target))

if __name__ == '__main__':
    test(candidates = [2,3,6,7], target = 7)
    test(candidates = [2,3,5], target = 8)
    test(candidates = [2], target = 1)
