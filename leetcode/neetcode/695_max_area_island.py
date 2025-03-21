class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int) -> int:
            nonlocal m, n
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

        maxArea = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea


def test(grid: list[list[int]], output: int):
    sol = Solution()
    res = sol.maxAreaOfIsland(grid)
    assert res == output

if __name__ == '__main__':
    test(grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]],
        output= 6)
    
    test(grid = [
        [0,0,0,0,0,0,0,0]],
        output= 0)