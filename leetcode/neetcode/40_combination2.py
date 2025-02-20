
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def dfs(index: int, currSet: list, total: int):
            if total == target:
                res.append(currSet.copy())
                return
            
            n = len(candidates)
            if index == n:
                return
            
            i = index
            while i < n:
                num = candidates[i]
                if num + total > target:
                    return
                if (i > index and num == candidates[i - 1]):
                    i += 1
                    continue
                currSet.append(num)
                dfs(i + 1, currSet, total + num)
                currSet.pop()
                i += 1


        dfs(0, [], 0)
        return res


def test(candidates: list, target: int):
    sol = Solution()
    print(sol.combinationSum2(candidates, target))


if __name__ == '__main__':
    test(candidates = [9,2,2,2,2,4,6,1,5], target = 8)
    #test(candidates = [2,5,2,1,2], target = 5)
    #test(candidates = [10,1,2,7,6,1,5], target = 8)