import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            d = - (x * x + y * y)
            if i < k:
                heapq.heappush(heap, (d, x, y))
            elif d > heap[0][0]:
                heapq.heappushpop(heap, (d, x, y))

        res = []
        for p in heap:
            res.append([p[1],p[2]])
        return res

def test(points: list[list[int]], k: int):
    sol = Solution()
    print(sol.kClosest(points, k))

if __name__ == '__main__':
    test(points = [[1,3],[-2,2]], k = 1)
    test(points = [[3,3],[5,-1],[-2,4]], k = 2)