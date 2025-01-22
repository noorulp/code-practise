from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    """minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    minStack.top()    
    print(minStack.getMin()) 
    """
    minStack = MinStack()
    minStack.push(2147483646)
    minStack.push(2147483646)
    minStack.push(2147483647)
    print(minStack.top())
    print(minStack.pop())
    print(minStack.getMin()) 
    print(minStack.pop())
    print(minStack.getMin()) 
    print(minStack.pop())
    minStack.push(2147483647)
    print(minStack.top())
    print(minStack.getMin())
    minStack.push(-2147483648)
    print(minStack.top())
    print(minStack.getMin())
    print(minStack.top())
    print(minStack.getMin())
    
    

