from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        tempStack = deque()
        indexStack = deque()
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(tempStack) == 0:
                tempStack.append(temp)
                indexStack.append(i)
            else:
                while len(tempStack) > 0 and temp > tempStack[-1]:
                    index = indexStack.pop()
                    output[index] = i - index
                    tempStack.pop()
                tempStack.append(temp)
                indexStack.append(i)
        return output

if __name__ == '__main__':
    sol = Solution()
    temperatures = [80,73,74,75,71,69,72,76,73]
    print(sol.dailyTemperatures(temperatures))
    temperatures = [30,40,50,60]
    print(sol.dailyTemperatures(temperatures))
    [30,60,90]
    print(sol.dailyTemperatures(temperatures))
    temperatures = [10,9,8,7,6,5,4,3,2,1]
    print(sol.dailyTemperatures(temperatures))
    