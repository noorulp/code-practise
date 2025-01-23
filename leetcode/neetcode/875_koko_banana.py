import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max = piles[0]
        sum = 0
        for pile in piles:
            if pile > max:
                max = pile
            sum += pile
        left = int(math.ceil(sum/h))
        right = max
        prev = -1
        while left <= right:
            mid = int( (left + right)/2 )
            numOfHours = 0
            for pile in piles:
                numOfHours += math.ceil(pile/mid)
            if numOfHours <= h:
                prev = mid
                right = mid - 1
            elif numOfHours > h:
                left = mid + 1
        return prev

if __name__ == '__main__':
    sol = Solution()
    piles = [3,6,7,11]
    h = 8
    print(sol.minEatingSpeed(piles,h))
    piles = [30,11,23,4,20]
    h = 5
    print(sol.minEatingSpeed(piles,h))
    piles = [30,11,23,4,20]
    h = 6
    print(sol.minEatingSpeed(piles,h))
    