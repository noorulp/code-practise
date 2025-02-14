import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(self.heap, num)
            else:
                if num > self.heap[0]:
                    heapq.heappushpop(self.heap, num)
    
    def add(self, val: int) -> int:
        n = len(self.heap)
        if n < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

def test(input1: list, input2: list):
    k = KthLargest(input2[0][0], input2[0][1])
    index = 1   
    n = len(input2)
    print(k.heap)
    while index < n:
        print(k.add(input2[index][0]))
        index += 1

if __name__ == '__main__':
    test(["KthLargest", "add", "add", "add", "add"], [[4, [7, 7, 7]], [2], [10], [9], [9]])