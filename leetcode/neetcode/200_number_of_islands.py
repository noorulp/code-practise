
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int):
            nonlocal m, n
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


def test(grid: list[list[str]], output: int):
    sol = Solution()
    res = sol.numIslands(grid)
    assert res == output

if __name__ == '__main__':
    test(grid = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]],
        output= 1)
    test(grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]], 
        output= 3)
    
    test(grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]], 
        output= 1
    )