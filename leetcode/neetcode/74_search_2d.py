class Solution:
    def search(self, matrix: list[list[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = int((right + left)/2)
            midrow = int(mid/cols)
            midcol = mid%cols
            midEle = matrix[midrow][midcol]
            if midEle == target:
                return True
            elif midEle > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    sol = Solution()
    print(sol.search(matrix, target))
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    sol = Solution()
    print(sol.search(matrix, target))