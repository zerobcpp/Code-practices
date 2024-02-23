class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        cache = {}
        def helper(i, status):
            if i >= N:
                return 0
            if (i, status) in cache:
                return cache[i, status]
            profit = helper(i+1, status)
            if status:
                profit = max(profit, helper(i+1, not status) - prices[i])
            else:
                profit = max(profit, helper(i+1, not status) + prices[i])
            
            return profit
        
        return helper(0, True)