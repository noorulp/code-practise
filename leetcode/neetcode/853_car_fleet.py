from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        num = 0
        ps = [[pos, sp] for pos,sp in sorted(zip(position, speed), reverse=True)]
        prevTime = -1
        for i, item in enumerate(ps):
            pos = item[0]
            sp = item[1]
            time = (target-pos)/sp
            if time > prevTime:
                prevTime = time
                num += 1
            
        return num  

if __name__ == '__main__':
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    sol = Solution()
    print(sol.carFleet(target, position, speed))