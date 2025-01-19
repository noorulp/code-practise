class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        if height[l] < height[r]:
            secondMax = height[l]
            l += 1
        else:
            secondMax = height[r]
            r -= 1
        while l < r:
            if height[l] < height[r]:
                if height[l] < secondMax:
                    water += secondMax - height[l]
                else:
                    secondMax = height[l]
                l += 1
            else:
                if height[r] < secondMax:
                    water += secondMax - height[r]
                else:
                    secondMax = height[r]
                r -= 1
        return water

if __name__ == '__main__':
    S = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(S.trap(height))
    height = [4,2,0,3,2,5]
    print(S.trap(height))
    height = [5,2,4,7,3,1,6,7]
    print(S.trap(height))