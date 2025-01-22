from collections import deque

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = deque()
        heights.append(0)
        for i, heights in enumerate(heights):
            pos = i
            while len(stack) > 0 and stack[-1][1] > heights:
                item = stack.pop()
                pos = item[0]
                area = (i - item[0]) * item[1]
                if area > maxArea:
                    maxArea = area
            stack.append([pos,heights])
        return maxArea

if __name__ == '__main__':
    sol = Solution()
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))
    heights = [1,2,2,5,1]
    print(sol.largestRectangleArea(heights))
    heights = [2,1,5]
    print(sol.largestRectangleArea(heights))
    heights = [2,1,2]
    print(sol.largestRectangleArea(heights))