from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        left = right = 0
        res = []
        while right < k:
            while queue and nums[ queue[-1] ] < nums[right]:
                queue.pop()
            queue.append(right)
            right += 1
        res.append(nums[queue[0]])
        left += 1
        while right < len(nums):
            while queue and nums[ queue[-1] ] < nums[right]:
                queue.pop()
            queue.append(right)
            if queue[0] < left:
                queue.popleft()
            res.append(nums[ queue[0] ])
            right += 1
            left += 1
        
        return res

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))