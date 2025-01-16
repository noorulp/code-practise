
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = sell - buy
        max = profit

        for price in prices:
            if price < buy: # new min resets buy/sell indexes
                buy = price
                sell = price
                profit = sell - buy
                if profit > max:
                    max = profit
            if price > sell: # new max changes only sell
                sell = price
                profit = sell - buy
                if profit > max:
                    max = profit

        return max

if __name__ == '__main__':
    prices = [2,10,1,3,5,1,6]
    sol = Solution()
    k = sol.maxProfit(prices)
    print(k)
