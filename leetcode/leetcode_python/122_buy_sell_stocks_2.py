
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = sell - buy
        total = profit
        prices.append(0) # add zero at the end so that prev last element can be a maxima if needed 
        n = len(prices)
        i = 1
        while i < n - 1:
            # sell at local maxima
            if prices[i-1] < prices[i] and prices[i] >= prices[i+1]:
                sell = prices[i]
                profit += sell - buy
            # buy at local minima
            if prices[i-1] >= prices[i] and prices[i] < prices[i+1]:
                buy = prices[i]
                sell = buy
            i += 1
        return profit

if __name__ == '__main__':
    prices = [0,5,5,6,2,1,1,3]
    sol = Solution()
    k = sol.maxProfit(prices)
    print(k)
