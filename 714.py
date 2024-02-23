class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        
        @cache
        def helper(i, b):
            if i >= N:
                return 0
            profit = helper(i+1, b)
            if not b:
                profit = max(profit, helper(i+1, not b) + prices[i])
            else:
                profit = max(profit, helper(i+1, not b) - prices[i] - fee)
            return profit
        
        return helper(0, True)
                
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        cache = {}
        
        def helper(i, b):
            if i >= N:
                return 0
            if (i, b) in cache:
                return cache[i, b]
            profit = helper(i+1, b)
            if not b:
                profit = max(profit, helper(i+1, not b) + prices[i])
            else:
                profit = max(profit, helper(i+1, not b) - prices[i] - fee)
            cache[i, b] = profit
            return profit
        
        return helper(0, True)
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, -prices[0]
        N = len(prices)
        profit = 0
        for i in range(1, N):
            ps, pb = sell, buy
            sell = max(ps, pb + prices[i] - fee)
            buy = max(pb, ps - prices[i])
        
        return sell
                
                