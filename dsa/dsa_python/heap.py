
class MinHeap:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.heap = []

    def swap(self, i: int, j: int):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def heapify(self, i: int):
        l = self.left(i)
        r = self.right(i)
        n = len(self.heap)
        smallest = i
        if l < n and self.heap[smallest] > self.heap[l]:
            smallest = l
        if r < n and self.heap[smallest] > self.heap[r]:
            smallest = r
        
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)


    def getMin(self):
        return self.heap[0]
    
    def insert(self, key: int) -> bool:
        n = len(self.heap)
        if n == self.maxSize:
            return False
        self.heap.append(key)
        i = n
        parent = self.parent(i)
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = self.parent(i)

        return True

    def deleteKey(self, key : int):
        self.heap[key] = float('-inf')
        self.heapify()
        self.pop()

    def pop(self):
        val = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heapify(0)
        return val

    def parent(self, i: int):
        return (i - 1) // 2
    
    def left(self, i: int):
        return i * 2 + 1
    
    def right(self, i: int):
        return i * 2 + 2

    def __str__(self):
        return str(self.heap)

def testHeap(arr: list[int]):
    n = len(arr)
    heap = MinHeap(n)
    for num in arr:
        heap.insert(num)
        print(heap)

    heap.pop()
    print(heap)
    

if __name__ == '__main__':
    arr = [2,3,8,5,10,1]
    testHeap(arr)