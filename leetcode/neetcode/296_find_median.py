import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = [] # stores 2nd half of sorted array
        self.maxHeap = [] # stores 1st half of sorted array
        

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0:
            self.maxHeap.append(-num)
            return
        
        if num > -self.maxHeap[0]: # if num > max of left half
            heapq.heappush(self.minHeap, num) # go to right half
        else:
            heapq.heappush(self.maxHeap, -num)  # go to left half
        
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        rightLen = len(self.minHeap)
        leftLen = len(self.maxHeap)
        n = rightLen + leftLen
        if n % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0])/2
        else:
            if rightLen > leftLen:
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]

def test(funcs: list, vals: list):
    median = MedianFinder()
    i = 1
    while i < len(vals):
        f = funcs[i]
        v = vals[i]
        if f == "addNum":
            median.addNum(v[0])
        else:
            print(median.findMedian())
        i +=1 

if __name__ == '__main__':
    test(["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"],
        [[], [1], [2], [], [3], [4], [3], [1], [0], []])