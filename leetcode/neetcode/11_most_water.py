class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            if height[l] < height[r]:
                area = (r-l) * height[l]
                l += 1
            else:
                area = (r-l) * height[r]
                r -= 1
            if area > maxArea:
                maxArea = area
        return maxArea


if __name__ == '__main__':
    S = Solution()
    height = [1,8,6,2,5,4,8,3,4]
    print(S.maxArea(height))
    height = [1,1]
    print(S.maxArea(height))