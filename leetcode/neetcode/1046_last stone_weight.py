import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [num * -1 for num in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            w = x - y
            if w < 0:
                heapq.heappush(heap, w)
        
        if heap:
            return heap[0] * -1
        return 0


def test(stones):
    sol = Solution()
    print(sol.lastStoneWeight(stones))

if __name__ == '__main__':
    test([2,7,4,1,8,1,13,20])
    test([1])
    test([])