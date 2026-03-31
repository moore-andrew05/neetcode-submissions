class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        l = 0
        r = 1

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            profit = sell - buy
            if profit > max_profit:
                max_profit = profit

            if profit < 0:
                l += 1
                continue

            r += 1
            
        return max_profit
            