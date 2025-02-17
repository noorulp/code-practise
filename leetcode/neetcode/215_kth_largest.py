import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)
        
        return heap[0]

def test(nums: list, k: int):
    sol = Solution()
    print(sol.findKthLargest(nums, k))


if __name__ == '__main__':
    test(nums = [3,2,1,5,6,4], k = 2)
    test(nums = [3,2,3,1,2,4,5,5,6], k = 4)