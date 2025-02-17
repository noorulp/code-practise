import heapq
from collections import deque

class Solution:
    def leastInterval2(self, tasks: list[str], n: int) -> int:
        hashMap = [0] * 26
        A = ord('A')
        for task in tasks:
            hashMap[ord(task) - A] += 1    
        # enter all values in a heap -> (count, task)
        heap = []
        for i, count in enumerate(hashMap):
            if hashMap[i]:
                heapq.heappush(heap, (-count, i))
        interval = 0
        intervalMap = [-n - 1] * 26
        queue = deque()
        while heap or queue:
            task = -1
                # satisfies interval condition
            if queue and interval - intervalMap[queue[0][1]] > n:
                count, task = queue.popleft()
            else:
                while len(heap) and interval - intervalMap[heap[0][1]] <= n:
                    queue.append(heapq.heappop(heap))
                if heap:
                    count, task = heapq.heappop(heap)
            if task > -1:    
                print(chr(task + 65), end= '->')
                intervalMap[task] = interval
                if count + 1:
                    heapq.heappush(heap, (count + 1, task))
            else:
                print('idle', end= '->')    
            interval += 1
        return interval

    def leastInterval(self, tasks: list[str], n: int) -> int:
        hashMap = [0] * 26
        maxf = 0
        maxCount = 0
        A = ord('A')
        for task in tasks:
            i = ord(task) - A
            hashMap[i] += 1
            if hashMap[i] > maxf:
                maxf = hashMap[i]
                maxCount = 1
            elif hashMap[i] == maxf:
                maxCount += 1
        
        numberOfIdles = (maxf - 1) * (n - maxCount + 1)
        remaining = len(tasks) - maxf * maxCount
        totalIdles = max(0, numberOfIdles - remaining)

        return totalIdles + len(tasks)


def test(tasks: list[str], n: int):
    sol = Solution()
    print()
    print(sol.leastInterval(tasks, n))
    


if __name__ == '__main__':
    test(tasks = ["A","A","A","B","B","B"], n = 2)
    test(tasks = ["A","C","A","B","D","B"], n = 1)
    test(tasks = ["A","A","A", "B","B","B"], n = 3)