from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = deque()
        hashSet = set()
        for coin in coins:
            if amount == coin:
                return 1
            if amount > coin:
                hashSet.add(amount - coin)
                queue.append(amount - coin)
        
        level = 2
        while queue:
            n = len(queue)
            while n:
                rem = queue.popleft() 
                for coin in coins:
                    if coin == rem:
                        return level
                    if rem > coin:
                        if (rem - coin) not in hashSet:
                            hashSet.add(rem - coin)
                            queue.append(rem - coin)
                n -= 1
            level += 1
        return -1

def test(coins: list, amount: int):
    sol = Solution()
    print(sol.coinChange(coins, amount))


if __name__ == '__main__':
    test(coins = [2], amount = 3)
    test(coins = [1,3,4,5,10], amount = 7)